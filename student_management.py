students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    
    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    
    for student in students:
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", student["marks"])
        print("--------------------")
    print()

def search_student():
    roll = input("Enter roll number to search: ")
    for student in students:
        if student["roll"] == roll:
            print("Student Found!")
            print(student)
            print()
            return
    print("Student not found.\n")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
