'''
Dat Tran
File name: M02 Lab.py
A program to store student's record (last name, first name, GPA)
and find students who qualify for either the Dean's List or the Honor Roll.
'''

class Student:
    def __init__(self, last_name, first_name, gpa):
        self.last_name = last_name
        self.first_name = first_name
        self.gpa = gpa

    def display(self):
        print("   " + self.last_name + " " + self.first_name + ": "+ str(self.gpa))
		
		
students = list()


#Adding Students record...
while True:
    last_name = input("Enter 'zzz' to quit. Enter last name: ")
    if last_name == 'zzz':
        print()
        break
    first_name = input("Enter first name: ")
    gpa = float(input("Enter gpa: "))
    print()
    students.append(Student(last_name, first_name, gpa))


deans_list = []  # Create an empty list for Dean's list
honor_roll = []  # Create an empty list for Honor Roll

# Check GPA for Dean's list and Honor Roll
for student in students:
    if student.gpa > 3.5:
        deans_list.append(student)
    if student.gpa > 3.25:
        honor_roll.append(student)

# Print Dean's list
if deans_list:
    print("Dean's List:")
    for student in deans_list:
        student.display()
else:
    print("There is no student in Dean's list.")

# Print Honor Roll
if honor_roll:
    print("Honor Roll:")
    for student in honor_roll:
        student.display()
else:
    print("There is no student in Honor Roll.")