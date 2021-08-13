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

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/video_lectures", methods=['GET', 'POST'])
def video_lectures():
    if request.method == 'POST':
        lectures = Lecture.query.filter_by(course = request.form['video_button']).all()
        print(lectures)
        return render_template('video_lectures.html', lectures = lectures)

if __name__ == '__main__':
    app.run(debug=True)