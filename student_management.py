print("=" * 40)
print("     STUDENT MANAGEMENT SYSTEM")
print("=" * 40)
print("\nMENU")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Exit")
choice = input("Enter your choice: ")
print("You selected:", choice)
students = []
name = input("Enter Name: ")
age = input("Enter Age: ")
course = input("Enter Course: ")
student = {
    "name": name,
    "age": age,
    "course": course
}

students.append(student)

print("Student added successfully!")
for student in students:
    print(student)
    search = input("Enter student name: ")
    for student in students:
    if student["name"] == search:
        print(student)
        student["course"] = input("New Course: ")
        students.remove(student)
        while True:
    # menu code

    if choice == "6":
        break
        else:
    print("Invalid Choice")
    {'name': 'Ali', 'age': '18', 'course': 'Science'}