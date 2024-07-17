import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user = os.getenv("MYSQL_USER"),
    password = os.getenv("MYSQL_PASSWORD"),
    host = os.getenv("MYSQL_HOST"),
    port = 3306
)

print(mydb)

#peewee model
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])
name = "Steven Cao"
 
@app.route('/')
def index():
    about_me = "Hey! My name is Steven cao. I'm a undergradute computer science student at the University of California, Irvine."
    markers  = [       
        {'lat': 33, 'lon': -118, 'popup': 'Los Angeles'},
        {'lat': 41, 'lon': -74, 'popup': 'New York'},
        {'lat': 18, 'lon': -155, 'popup': 'Hawaii'},
    ]
    return render_template('map.html', name=name, title="About", about=about_me, markers=markers, url=os.getenv("URL"))

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
    hobbies = ["Reading books", "Running", "Biking", "Hiking", "Playing Ping Pong"]
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



# POST route which adds a timeline post
@app.route('/api/timeline_post', methods = ["POST"])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

#GET endpoint that retrieves all timeline posts ordered by created_at descending so the newest timeline posts are returned at the top
@app.route('/api/timeline_post', methods=["GET"])
def get_time_line_post():
    return {
        'timeline_posts' : [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }