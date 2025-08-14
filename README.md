Student Management System (Python)

A simple console-based application written in Python for managing student records.
Built as a beginner project to learn Python basics, CRUD operations, and JSON file storage.

✨ Features

Add Student – Store Roll No, Name, Grade, and Age.

View All Students – See all records in a table format.

Search Student – Find by Roll Number.

Update Student – Edit existing details.

Delete Student – Remove a record with confirmation.

Persistent Storage – Data saved in data.json so it survives program restarts.

🛠️ Prerequisites

Python 3.8+ installed

Code editor (VS Code, PyCharm, etc.)

📂 Project Structure

student-management/
├─ student_mgmt.py    # Main program
├─ data.json          # Student data (auto-created when you run)
└─ README.txt         # Project details


🚀 How to Run

Clone or download this project

git clone https://github.com/bala-anjaneyulu/student-management.git
cd student-management


Run the program

python student_mgmt.py


📸 Sample Output

===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice: 1
--- Add New Student ---
Enter Roll Number: 101
Enter Name: Alice
Enter Grade: A
Enter Age (optional): 15
✅ Student added successfully!


📖 What I Learned

Using Python lists & dictionaries to store structured data.

Creating functions to organize code.

JSON file handling for saving/loading data.

Input validation and preventing duplicate records.

Building a menu-based console application.

🔮 Future Improvements

Search by name (partial match)

Sort records by Roll No or Name

Export data to CSV

Use SQLite database instead of JSON

Add GUI with Tkinter

Web version using Flask
