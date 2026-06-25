# class_demo.py

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Student Details")
        print("----------------")
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Course :", self.course)


# Object Creation
student1 = Student("Godwin", 21, "Computer Engineering")

student1.display()