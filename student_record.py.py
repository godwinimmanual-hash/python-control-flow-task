# student_record.py

students = {}

while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        students[roll] = {
            "Name": name,
            "Marks": marks
        }

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("----------------------------")
            for roll, details in students.items():
                print(f"Roll No : {roll}")
                print(f"Name    : {details['Name']}")
                print(f"Marks   : {details['Marks']}")
                print("----------------------------")

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        if roll in students:
            print("\nStudent Found")
            print("-------------")
            print("Name :", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")