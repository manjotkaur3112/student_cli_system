# Student CLI Application

## 📌 Project Overview

The **Student CLI Application** is a command-line based student management system developed using **Python**. 
It allows users to manage student records stored in a CSV file. 
The application provides features to add, view, update, search, and delete student information along with subject-wise marks and CGPA.

---

## 🚀 Features

* Add new student records
* Assign subjects based on the selected branch
* Enter subject-wise marks
* Automatically calculate CGPA
* View all student records
* Update student name or age
* Update student marks and CGPA
* Search students by:

  * Roll Number
  * Name
  * Age
  * Gender
  * Branch
  * Marks
* Delete student records
* Store data permanently in a CSV file

---

## 🛠️ Technologies Used

* Python 3
* CSV Module (Built-in)

---

## 📂 Project Structure

```
student_cli_app/
│
├── main.py                 # Main Python program
├── studentData.csv         # Stores student records
└── README.md               # Project documentation
```

## ⚙️ How to Run the Project

### Step 1: Clone or Download the Project

```
git clone <repository-link>
```

Or download the project as a ZIP file.

### Step 2: Open the Project Folder

Open the project folder in your terminal or command prompt.

### Step 3: Run the Application

```
python main.py
```

---

## 💾 Data Storage

Student records are stored in a CSV file named:

```
studentData.csv
```

This file is automatically updated whenever a student is added, updated, or deleted.

---

## 📌 Functions Used

| Function           | Description                                 |
| ------------------ | ------------------------------------------- |
| `save_data()`      | Saves all student records to the CSV file   |
| `add_student()`    | Adds a new student with subject-wise marks  |
| `view_student()`   | Displays all student records                |
| `update_student()` | Updates student name or age                 |
| `update_marks()`   | Updates subject marks and recalculates CGPA |
| `search_student()` | Searches students using different fields    |
| `delete_student()` | Deletes a student record                    |

---

## 🔮 Future Improvements

* Replace CSV with a MySQL database.
* Add login and Registration.
* Export student reports.

---

## 👨‍💻 Editor

**Manjot Kaur**

Python Student CLI Application using CSV for student record management.
