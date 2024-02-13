
import os
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from flask import Flask, render_template, request, redirect, make_response, jsonify,session
import requests, json
import mysql.connector
# from user_methods import hash_sha_256
# from Final_lang import get_video_links

from final import get_video_links, hash_sha_256, main



mydb = mysql.connector.connect(
    host="localhost",
    database="study",
    user="root",
    password="Manhvi@"
)
cursor = mydb.cursor()

load_dotenv()

app=Flask(__name__)
app.secret_key = 'secretkeyfordungeon'

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN= os.environ.get('TWILIO_AUTH_TOKEN')
VERIFY_SERVICE_SID= os.environ.get('VERIFY_SERVICE_SID')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title="home")

@app.route('/user_login',methods=['GET','POST'])
def user_login():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['passwd']
        cursor.execute('select * from students where username="{0}" and password="{1}"'.format(username,hash_sha_256(password)))
        data=cursor.fetchall()
        if(data):
            resp=make_response(render_template('login.html',title='login-success'))
            resp.set_cookie('user',username)
            return resp
        else:
            return redirect('/')

@app.route('/user_signup',methods=['GET','POST'])
def user_signup():
    if request.method=="POST":
        data=[]
        data.append(request.form['fname'])
        data.append(request.form['email'])
        data.append(request.form['phone'])
        data.append(request.form['username'])
        data.append(request.form['password'])
        # print(data)
        password=request.form['password']
        cnfm_password=request.form['cnfmpassword']
        if password!=cnfm_password:
            return redirect('/')
        else:
            session['user_data']=data
            print(session['user_data'])
            send_verification(data[2])
            return redirect('/otp_verification')
            # return render_template('verifyOTP.html',title='verify-otp')

@app.route('/otp_verification')
def otp_verification():
    return render_template('verifyOTP.html',title='verify-otp')

@app.route('/verify_otp', methods=['GET','POST'])
def verify_otp():
    print("UserData from session", session['user_data'])
    if request.method=="POST":
        rec_otp=request.form['rec_otp']
        if check_verification_token(session['user_data'][2], rec_otp):
            cursor.execute('insert into students values ("{0}","{1}","{2}","{3}","{4}")'.format(session['user_data'][3],session['user_data'][0],session['user_data'][1],hash_sha_256(session['user_data'][4]),session['user_data'][2]))
            mydb.commit()
            session.clear()
            return render_template('acc_created.html',title="success")
        else:
            return redirect('/')
        
def send_verification(phone):
    # print("\nin send ver.\n")
    client.verify \
        .services(VERIFY_SERVICE_SID) \
        .verifications \
        .create(to=phone, channel='sms')
    
def check_verification_token(phone, token):
    check = client.verify \
        .services(VERIFY_SERVICE_SID) \
        .verification_checks \
        .create(to=phone, code=token)    
    return check.status == 'approved'
        

@app.route('/courses_offered')
def courses_offered():
    return render_template('courses.html',title='courses-offered')

# @app.route('/save_score/<score>')
# def save_score(score):
#     # print('\nscore: {0}\n'.format(score))
#     try:
#         cursor.execute('insert into scores values("{0}","{1}",{2},{3})'.format(request.cookies.get('user'),quiz_topic,score,len(quiz_questions)))
#         mydb.commit()
#     except Exception as error:
#         print(error)
#     return redirect('/')
        
@app.route('/default_quiz')
def default_quiz():
    topic='CSS'
    cursor.execute('select * from default_quiz where topic="{0}"'.format(topic))
    quiz_data=cursor.fetchall()
    print(quiz_data)
    return render_template('quiz.html',quiz_data=quiz_data)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = request.form.to_dict(flat=False)
    score = calculate_score(user_answers)
    if (cursor.execute('select * from score where username={0} and quiz_topic={1}'.format(request.cookies.get('user'),'default_quiz'))):
        cursor.execute('update scores set total_score={0} where username={1}'.format(score,request.cookies.get('user')))
    else:
        cursor.execute('insert into scores values("{0}","{1}","{2}","{3}")'.format(request.cookies.get('user'),'default_quiz',score,len(user_answers)))
        mydb.commit()
    return render_template('result.html', score=score, total_questions=len(user_answers))

def calculate_score(user_answers):
    score = 0
    for i, user_answer in user_answers.items():
        # Retrieve the correct answer from the database
        cursor.execute("SELECT correct_option FROM default_quiz WHERE question_no = {0}".format(int(i.split('_')[1])))
        # print(cursor)
        correct_answer = cursor.fetchone()[0]

        if user_answer[0] == correct_answer:
            score += 1
    print(score)
    # return score
    return score

@app.route('/selected_courses/<topic>')
def course_offered(topic):
    # topic=request.args.get('topic')
    print(topic)
    video_links=get_video_links(topic)
    print(video_links)
    # session['vid_lnk']=video_links
    return render_template('video_links.html',title='video-to-learn',data=video_links)

# @app.route('/')

@app.route('/course_video/<link>')
def course_video(link):
    print(link)
    return render_template('video.html',title='show-video',link=link+)
    # link=request.args.get('link')
    # print(link)
    request.cookies.get('link')
    # link=request.
    return redirect('/showing_video')

@app.route('/showing_video')
def showing_video():
    render_template('video.html',title='video-show',link=request.cookies.get('link'))

@app.route('/myprofile')
def myprofile():
    cursor.execute('select * from students where username="{0}"'.format(request.cookies.get('user')))
    data=cursor.fetchall()
    return render_template('profile.html',data=data[0],title=request.cookies.get('user'))

@app.route('/mycourses')
def mycourses():
    cursor.execute('select * from courses where username="{0}"'.format(request.cookies.get('user')))
    data=cursor.fetchall()
    return render_template('mycourses.html',data=data,title='mycourses-{}'.format(request.cookies.get('user')))

@app.route('/help_center')
def help_center():
    return render_template('help.html',title="help-center")

@app.route('/logout')
def logout():
    response = make_response(render_template('logout.html',title='logged-out'))
    response.set_cookie('user', '', max_age=0)
    return response

if __name__=="__main__":
    app.run(debug=True)