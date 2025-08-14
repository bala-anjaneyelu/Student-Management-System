# student_mgmt.py
import json
import os

DATA_FILE = "data.json"
#Load student data from JSON file if it exists.
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []
#Save current student list to JSON file.
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)
#Find a student by roll number
def search_student(roll):
    for s in students:
        if s['roll_no'] == roll:
            return s
    return None
#Add a new student record.
def add_student():
    roll = input("Roll no: ").strip()
    if not roll:
        print("Roll no cannot be empty.")
        return
    if any(s['roll_no'] == roll for s in students):
        print("Roll no already exists.")
        return
    name = input("Name: ").strip()
    grade = input("Grade: ").strip()
    age = input("Age (optional): ").strip()

    students.append({
        "roll_no": roll,
        "name": name,
        "grade": grade,
        "age": age if age else None
    })
    print("Student added.")
#Display all student records
def view_students():
    if not students:
        print("No records found.")
        return
    print(f"{'Roll':<10}{'Name':<20}{'Grade':<6}{'Age':<5}")
    print("-" * 45)
    for s in students:
        age_str = s['age'] if s['age'] else "-"
        print(f"{s['roll_no']:<10}{s['name']:<20}{s['grade']:<6}{age_str:<5}")
#Search for a student by roll number.
def search_menu():
    roll = input("Enter roll number: ").strip()
    student = search_student(roll)
    if student:
        print(f"Found: {student}")
    else:
        print("Not found.")
#Update details of a student
def update_student():
    roll = input("Roll no to update: ").strip()
    student = search_student(roll)
    if not student:
        print("Not found.")
        return

    new_name = input(f"Name [{student['name']}]: ").strip()
    if new_name:
        student['name'] = new_name

    new_grade = input(f"Grade [{student['grade']}]: ").strip()
    if new_grade:
        student['grade'] = new_grade

    new_age = input(f"Age [{student['age'] if student['age'] else '-'}]: ").strip()
    if new_age:
        student['age'] = new_age

    print("Student updated.")
#Delete a student record.
def delete_student():
    roll = input("Roll no to delete: ").strip()
    student = search_student(roll)
    if not student:
        print("Not found.")
        return
    confirm = input("Are you sure? (y/N): ").lower()
    if confirm == "y":
        students.remove(student)
        print("Student deleted.")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1) Add Student")
        print("2) View Students")
        print("3) Search Student")
        print("4) Update Student")
        print("5) Delete Student")
        print("6) Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_menu()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            save_data()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    students = load_data()
    main()
