# Student Record Management System

students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")

    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\nList of Students:")
    for student in students:
        print(
            f"ID: {student['student_id']}, "
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Course: {student['course']}"
        )
    print()

def search_student():
    search_id = input("Enter Student ID to search: ")

    for student in students:
        if student["student_id"] == search_id:
            print("\nStudent Found:")
            print(f"ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}\n")
            return

    print("Student not found.\n")

def main_menu():
    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

main_menu()
