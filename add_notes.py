from app import db, Notes
from datetime import datetime

notes = Notes.query.all()
print(notes)

while(True):

    course = input("Enter course: ")
    notes_name = input("Enter name: ")
    provided_by = input("Enter the provider: ")
    till_date = datetime.strptime(input("Enter the date: "), "%d-%m-%Y")
    notes_link = input("Enter the link: ")

    new_notes = Notes(course = course, notes_name = notes_name, notes_link = notes_link, provided_by = provided_by, till_date = till_date)
    db.session.add(new_notes)

    print("Do you want to add more notes?")
    if(input() == 'y'):
        continue
    else:
        break

print("Do you want to commit these changes?")
if(input() == 'y'):
    db.session.commit()
else:
    pass

