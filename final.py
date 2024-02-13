import requests
import isodate
import subprocess
from moviepy.editor import VideoFileClip
import os
import moviepy.editor as mp
from transformers import AutoModelWithLMHead, AutoTokenizer
from torch import tensor,argmax
from transformers import BertTokenizer
from transformers import BertForQuestionAnswering
import random
import pandas as pd
import whisper
import hashlib
def get_video_links(query):
    
    api_url = f"https://www.googleapis.com/youtube/v3/search?key=AIzaSyCs7DViYb2rJmKW_R4xODNqeDThEnLJeyA&q={query}&part=snippet&type=video&maxResults=20"

    video_links = []
    try:
        response = requests.get(api_url)
        data = response.json()
        videos = data.get("items", [])
        for video in videos:
            video_id = video["id"]["videoId"]
            video_link = f"https://www.youtube.com/watch?v={video_id}"

            video_details_url = f"https://www.googleapis.com/youtube/v3/videos?key=AIzaSyCs7DViYb2rJmKW_R4xODNqeDThEnLJeyA&id={video_id}&part=contentDetails,snippet"
            details_response = requests.get(video_details_url)
            details_data = details_response.json()

            duration_iso = details_data["items"][0]["contentDetails"]["duration"]

            duration_seconds = isodate.parse_duration(duration_iso).total_seconds()

            video_language = details_data["items"][0]["snippet"].get("defaultLanguage", "")
            if duration_seconds > 800 and video_language.lower() == "en": 
                video_links.append(video_link)

    except requests.RequestException as e:
        print("Error fetching data:", e)
    return video_links


def download_video(video_url, duration):
    # First, download the entire video with yt-dlp
    temp_output_path = 'temp_video.mp4'
    command = [
        'yt-dlp',
        '--merge-output-format', 'mp4',
        '-o', temp_output_path,
        video_url
    ]
    subprocess.run(command)

    # Then, use ffmpeg to extract the desired part
    output_path = 'output.mp4'
    command = [
        'ffmpeg',
        '-i', temp_output_path,
        '-t', str(duration),
        '-c', 'copy',
        output_path
    ]
    subprocess.run(command)

    # Optionally, delete the temporary video file
    os.remove(temp_output_path)

    return output_path




class VideoConverter:
    def __init__(self, video_path):
        self.video_path = video_path
        self.output_dir = "Audios"

    def convert_to_audio(self):
        try:
            if not os.path.exists(self.video_path):
                raise FileNotFoundError("Video file not found.")

            if not os.path.isfile(self.video_path):
                raise ValueError("Invalid video file path.")

            print("Converting to Audio .......")
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)

            # Extract audio from video and save as WAV file
            audio_filename = os.path.splitext(os.path.basename(self.video_path))[0] + ".wav"
            audio_path = os.path.join(self.output_dir, audio_filename)

            video = mp.VideoFileClip(self.video_path)
            video.audio.write_audiofile(audio_path)
            video.close()  # Close the VideoFileClip
            absolute_path = os.path.abspath(audio_path)
            return absolute_path

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error occurred during audio conversion: {e}")
class AudioTranscriber:
    def __init__(self, model_name="large"):
        print("loading the model")
        self.model = whisper.load_model(model_name)

    def transcribe_audio(self, path_audio):
        print("Converting to Text .......")
        result = self.model.transcribe(path_audio)
        transcribed_text = result["text"]

        output_folder = "Transcribed_Text"
        os.makedirs(output_folder, exist_ok=True)

        audio_filename = os.path.splitext(os.path.basename(path_audio))[0]
        text_filename = f"{audio_filename}.txt"
        output_path = f"{output_folder}/{text_filename}"

        with open(output_path, "w") as file:
            file.write(transcribed_text)

        absolute_path = os.path.abspath(output_path)
        return transcribed_text, absolute_path
tokenizer_q = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-question-generation-ap")
model_q = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-question-generation-ap")
model_a = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer_a = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

def answer_question(question, context):
    context_parts = [context[i:i+512] for i in range(0, len(context), 512)]

    answers = []
    for part in context_parts:
        input_ids = tokenizer_a.encode(question, part)
        sep_index = input_ids.index(tokenizer_a.sep_token_id)
        num_seg_a = sep_index + 1
        num_seg_b = len(input_ids) - num_seg_a
        segment_ids = [0]*num_seg_a + [1]*num_seg_b
        assert len(segment_ids) == len(input_ids)
        outputs = model_a(tensor([input_ids]),
                        token_type_ids=tensor([segment_ids]),
                        return_dict=True)
        start_scores = outputs.start_logits
        end_scores = outputs.end_logits
        answer_start = argmax(start_scores)
        answer_end = argmax(end_scores)
        tokens = tokenizer_a.convert_ids_to_tokens(input_ids)
        answer = tokens[answer_start]
        for i in range(answer_start + 1, answer_end + 1):
            if tokens[i][0:2] == '##':
                answer += tokens[i][2:]
            else:
                answer += ' ' + tokens[i]
        answers.append(answer)


    return max(answers, key=lambda ans: ans[0])


def get_questions(context, max_length=64):
    qns = []
    sentences = context.split('.')
    for sentence in sentences[:-1]:
        input_text = "answer: %s  context: %s </s>" % ('', sentence)
        features = tokenizer_q([input_text], return_tensors='pt')

        output = model_q.generate(input_ids=features['input_ids'],
                   attention_mask=features['attention_mask'],
                   max_length=max_length)
        qns.append(tokenizer_q.decode(output[0]).replace('<pad> question: ','').replace('</s>',''))
    return qns  # Make sure to return the list of quest
def interactive_mcq_questions(context, user_name, num_options=4, num_questions=5):
    questions = get_questions(context)
    sentences = context.split('.')
    question_count = 0
    score = 0
    scores = {}
    for question in questions:
        if question_count >= num_questions:
            break
        correct_answer = answer_question(question, context)
        options = [correct_answer]
        while len(options) < num_options:
            fake_answer = random.choice(sentences)
            if fake_answer not in options:
                options.append(fake_answer)
        random.shuffle(options)
        print(f"Question: {question}")
        for j, option in enumerate(options, start=1):
            print(f"\t{j}. {option}")
        user_answer = input("\nPlease choose the correct option (1-4): ")
        if options[int(user_answer)-1] == correct_answer:
            print("Correct! \n")
            score += 1
        else:
            print(f"Oops! That's not correct. The correct answer was: {correct_answer}\n")
        question_count += 1
    scores[user_name] = score
    print(f"{user_name}, your total score is {score} out of {num_questions}")  

    if score<3:
        pass
    else:
        pass 


def main():
    search_query = input("Enter your search query: ")
    video_links = get_video_links(search_query)
    if video_links:
        for i, video_link in enumerate(video_links):
            print(f"{i+1}: {video_link}")
        selected_video = int(input("Enter the number of the video you want to download: ")) - 1

        download_whole = input("Do you want to download the whole video? (yes/no): ")
        if download_whole.lower() == 'no':
            
            end_time = input("Enter the end time in seconds: ")
            video_path = download_video(video_links[selected_video], end_time)
        else:
            video_path = download_video(video_links[selected_video])

        
    else:
        print("No video links found for the given search query.")

    converter = VideoConverter(video_path)
    audio_path = converter.convert_to_audio()

    transcriber = AudioTranscriber()
    transcribed_text, _ = transcriber.transcribe_audio(audio_path)

    user_name = input("Enter your name: ")
    interactive_mcq_questions(transcribed_text, user_name)


def hash_sha_256(data):
    data=bytes(data,'utf-8')
    sha=hashlib.sha256()
    sha.update(data)
    return sha.hexdigest()



if __name__ == "__main__":
    main()
