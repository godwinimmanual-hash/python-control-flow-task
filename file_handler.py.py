# file_handler.py

def save_student(student):
    with open("students.txt", "a") as file:
        file.write(f"{student.roll_no},{student.name},{student.marks}\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
            else:
                print("\nStudent Records")
                print("---------------------------")
                for line in data:
                    roll, name, marks = line.strip().split(",")
                    print(f"Roll No : {roll}")
                    print(f"Name    : {name}")
                    print(f"Marks   : {marks}")
                    print("---------------------------")

    except FileNotFoundError:
        print("No records found.")