# dictionary_demo.py

student = {
    "Roll No": 101,
    "Name": "Godwin",
    "Age": 21,
    "Course": "Computer Engineering",
    "CGPA": 8.95
}

print("Student Details")
print("----------------")

for key, value in student.items():
    print(f"{key}: {value}")

print("\nUpdating CGPA...")
student["CGPA"] = 9.10

print("Updated Student Details")
print("-----------------------")

for key, value in student.items():
    print(f"{key}: {value}")