import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

name = "Steven Cao"

@app.route('/')
def index():
    about_me = "Hey! My name is Steven cao. I'm a undergradute computer science student at the University of California, Irvine."
    markers  = [       
        {'lat': 33, 'lon': -118, 'popup': 'Los Angeles'},
        {'lat': 41, 'lon': -74, 'popup': 'New York'},
        {'lat': 18, 'lon': -155, 'popup': 'Hawaii'},
    ]
    return render_template('index.html', name=name, title="About", about=about_me, markers=markers, url=os.getenv("URL"))

@app.route('/education')
def education():
    educations = [
        {
            'school': "UC Irvine",
            'degree': "B.S. in Computer Science, Minor in Mathematics",
            'start_date': "September 2023",
            'end_date': "June 2027",
            'description': "Majoring in Computer Science and Mathematics at UC Irvine"
        }
    ]
    return render_template('education.html', name=name, title="Education", educations = educations, url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    hobbies = ["Reading books", "Playing Ping Pong", "Running", "Biking", "Hiking"]
    return render_template('hobbies.html', name=name, title="Hobbies", hobbies=hobbies, url=os.getenv("URL"))

@app.route('/work_experiences')
def work_experiences():
    experiences = [
        {
        'position': "Undergraduate Student Researcher",
        'company': "UCI Samueli School of Engineering",
        'start_date': "September 2023",
        'end_date': "Present",
        'description': "Developed deep learning models using EEGNet and InceptionTime for biometric identification and mTBI detection"
        }
    ]
    return render_template('work_experiences.html', name=name, title="Work Experiences", work_experiences=experiences, url=os.getenv("URL"))
