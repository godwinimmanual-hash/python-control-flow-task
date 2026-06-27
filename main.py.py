# main.py

from student import Student
from file_handler import save_student, view_students

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        student = Student(roll, name, marks)

        save_student(student)

        print("Student added successfully!")

    elif choice == "2":

        view_students()

    elif choice == "3":

        print("Thank you!")
        break

    else:
        print("Invalid Choice.")