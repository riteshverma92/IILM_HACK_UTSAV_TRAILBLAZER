import requests
import isodate

def get_video_links(query):
    api_url = f"https://www.googleapis.com/youtube/v3/search?key=AIzaSyAtStIA5edlw87Br46xbiaB8K9RrNW6_6I&q={query}&part=snippet&type=video&maxResults=20"
    video_links = []  

    try:
        response = requests.get(api_url)
        data = response.json()
        videos = data.get("items", [])
        for video in videos:
            video_id = video["id"]["videoId"]
            video_link = f"https://www.youtube.com/watch?v={video_id}"

            video_details_url = f"https://www.googleapis.com/youtube/v3/videos?key=AIzaSyAtStIA5edlw87Br46xbiaB8K9RrNW6_6I&id={video_id}&part=contentDetails,snippet"
            details_response = requests.get(video_details_url)
            details_data = details_response.json()

            duration_iso = details_data["items"][0]["contentDetails"]["duration"]
            duration_seconds = isodate.parse_duration(duration_iso).total_seconds()
            video_language = details_data["items"][0]["snippet"].get("defaultLanguage", "")
            
            if duration_seconds > 900 and video_language.lower() == "en": 
                video_links.append(video_link)  

    except requests.RequestException as e:
        print("Error fetching data:", e)

    return video_links  
if __name__ == "__main__":
    search_query = input("Enter your search query: ")
    links = get_video_links(search_query)
    print(links) 