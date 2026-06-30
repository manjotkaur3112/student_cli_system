import csv

student = []

fieldNames = ["RollNo","Name","Age","Gender","Branch","Marks","CGPA"]

def save_data(student):
    with open("studentData.csv","w",newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(student)

def add_student():
    try:
        name = input("Enter student name: ")
        rollNo = int(input("Enter student rollno: "))
        age = int(input("Enter student age: "))
        Gender = ["Male","Female","Other"]
        print("Select Gender: ",Gender)
        choice = int(input("Enter your choice in no. format: "))
        if choice == 1:
            gender = "Male"
        elif choice == 2:
            gender = "Female"
        elif choice == 3:
            gender = "Other"
        else:
            gender = "Invalid Choice"
        print("Your gender: ",gender)

        Branch = ["CSE","IT","ECE","ME"]
        Subjects = {
            "CSE": ["Python","DBMS","Operating System","Computer Networks","DSA"],
            "IT":["Python","Web Development","DBMS","Cloud Computing"],
            "ECE": ["Digital Electronics","Signals","Microprocessors"],
            "ME": ["Thermodynamics","Machine Design","Fluid Mechanics"]
            }
        print("Select Branch: ",Branch)
        choice = int(input("Enter your choice in no. format: "))
        if choice == 1:
            branch = "CSE"
        elif choice == 2:
            branch = "IT"
        elif choice == 3:
            branch = "ECE"
        elif choice == 4:
            branch = "ME"
        else:
            branch = "Invalid Choice"

        marks = {}
        print("Enter marks for each subject: ")
        for subject in Subjects[branch]:
            mark = int(input(f"{subject}: "))
            marks[subject] = mark
        
        total = sum(marks.values())
        percentage = total/len(marks)
        cgpa = round(percentage/9.5,2)

        with open("studentData.csv","a",newline="") as file:
            fieldNames = ["RollNo","Name","Age","Gender","Branch","Marks","CGPA"]
            writer = csv.DictWriter(file,fieldnames=fieldNames)
            writer.writerow({"RollNo": rollNo,"Name": name,"Age": age,"Gender": gender,"Branch": branch,"Marks": marks,"CGPA": cgpa})
        print("Student added successfully")

    except ValueError:
        print("Invalid input value")

def view_student():
    try:
        with open("studentData.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print("-"*45)
                print("RollNo: ", row["RollNo"])
                print("Name: ", row["Name"])
                print("Age: ", row["Age"])
                print("Gender: ", row["Gender"])
                print("Branch: ", row["Branch"])
                print("\nMarks: ")
                marks = eval(row["Marks"])
                for subject in marks:
                    print(subject,": ",marks[subject])
                print("\nCGPA :", row["CGPA"])
    except FileNotFoundError:
        print("File not found")

def update_student():
    try:            
        updateByRollNo = int(input("Update By Roll Number: "))
        print("1. Update Age: ")
        print("2. Update Name: ")
        choice = int(input("Enter Your Choice what you want to update name or age: "))

        student = []
        with open("studentData.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["RollNo"] == str(updateByRollNo): 
                    if choice == 1:
                        row["Age"] = input("Enter updated age of student: ")
                        print("Student Age Updated Successfully")
                    elif choice == 2:
                        row["Name"] = input("Enter updated name of the student: ")
                        print("Student name updated successfully")
                student.append(row)
        save_data(student)

    except FileNotFoundError:
        print("file not found")

def update_marks():
    try:
        updateByRollNo = int(input("Update student marks by there roll no: "))
        student = []

        Subjects = {
            "CSE": ["Python","DBMS","Operating System","Computer Networks","DSA"],
            "IT":["Python","Web Development","DBMS","Cloud Computing"],
            "ECE": ["Digital Electronics","Signals","Microprocessors"],
            "ME": ["Thermodynamics","Machine Design","Fluid Mechanics"]
            }
        
        found = False
        
        with open("studentData.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["RollNo"] == str(updateByRollNo):
                    found = True
                    branch = row["Branch"]
                    subjects = Subjects[branch]
                    marks = {}
                    total = 0
                    for subject in subjects:
                        mark = int(input(f"{subject}: "))
                        marks[subject] = mark
                        total += mark

                    percentage = total/len(subject)
                    cgpa = round(percentage/10,2)

                    row["Marks"] = str(marks)
                    row["CGPA"] = cgpa
                
                student.append(row)
                if found:
                    save_data(student)
                    print("Student Marks Updated Successfully.")
                else:
                    print("Student rollNo not found")

    except FileNotFoundError:
        print("File Not Found")

def search_student():
    try:
        searchByValue = input("Enter Value For Search: ")
        found = False
        with open("studentData.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if searchByValue == row["Age"] or searchByValue == row["RollNo"] or searchByValue.lower() in row["Name"].lower() or searchByValue in row["Gender"].lower() or searchByValue in row["Branch"].lower() or searchByValue in row["Marks"]:
                    print("-"*45)
                    print("RollNo: ", row["RollNo"])
                    print("Name: ", row["Name"])
                    print("Age: ", row["Age"])
                    print("Gender: ", row["Gender"])
                    print("Branch: ", row["Branch"])
                    print("\nMarks: ")
                    marks = eval(row["Marks"])
                    for subject in marks:
                        print(subject,": ",marks[subject])
                    print("\nCGPA :", row["CGPA"])
                    found = True
            if not found:
                print("Student not found")

    except FileNotFoundError:
        print("File not found")

def delete_student():
    try:
        deleteByRollNo = input("Delete student data by entering the roll no: ")
        student = []
        found = False
        with open("studentData.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["RollNo"] == deleteByRollNo:
                    found = True
                else:
                    student.append(row)
        
        if found:
            save_data(student)
            print("Student deleted successfully")
        else:
            print("Student not found")
        
    except FileNotFoundError:
        print("File not found")

while True:
    print("*********** Student CLI APP **********")
    print("1. Add Student: ")
    print("2. View Student: ")
    print("3. Update Student: ")
    print("4. Update Student Marks: ")
    print("5. Search Student: ")
    print("6. Delete Student: ")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        search_student()
    elif choice == 6:
        delete_student()
    elif choice == 7:
        print("End Program")
        break
    else:
        print("Invalid choice")