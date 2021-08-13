from app import db, Lecture
from datetime import datetime

lectures = Lecture.query.all()
print(lectures)

while(True):

    course = input("Enter course: ")
    lecture_name = input("Enter name: ")
    lecture_link = input("Enter the link: ")
    lecture_date = datetime.strptime(input("Enter the date: "), "%Y-%m-%d %H-%M-%S")

    new_lecture = Lecture(course = course, lecture_name = lecture_name, lecture_link = lecture_link, lecture_date = lecture_date)
    db.session.add(new_lecture)

    print("Do you want to add more lectures?")
    if(input() == 'y'):
        continue
    else:
        break

print("Do you want to commit these changes?")
if(input() == 'y'):
    db.session.commit()
else:
    pass

