from enum import unique
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(20), nullable = False)
    lecture_name = db.Column(db.String(30), nullable = False)
    lecture_link = db.Column(db.Text(), unique=True, nullable = False, default='#')
    lecture_date = db.Column(db.DateTime())

    def __repr__(self):
        return f"Lecture('{self.id}', '{self.lecture_name}', '{self.course}', '{self.lecture_date}', '{self.lecture_link}')"

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(20), nullable = False)
    notes_name = db.Column(db.String(30), nullable = False)
    notes_link = db.Column(db.Text(), unique=True, nullable = False, default='#')
    provided_by = db.Column(db.String(100), nullable = False, default='Anonymous')
    till_date = db.Column(db.DateTime())

    def __repr__(self):
        return f"Notes('{self.id}', '{self.notes_name}', '{self.course}', '{self.provided_by}', '{self.till_date}')"

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/video_lectures/<course>", methods=['GET', 'POST'])
def video_lectures(course):
    lectures = Lecture.query.filter_by(course = course).all()
    print(lectures)
    return render_template('video_lectures.html', lectures = lectures)

@app.route("/notes/<course>", methods=['GET', 'POST'])
def notes(course):
    notes = Notes.query.filter_by(course = course).all()
    print(notes)
    return render_template('notes.html', notes = notes)

@app.route("/timetable")
def timetable():
    return render_template('timetable.html')

if __name__ == '__main__':
    app.run(debug=True)