students = []

def add_student(roll_no, name, department):
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student with this Roll No already exists.")
            return False
            
    student = {
        "roll_no": roll_no, 
        "name": name, 
        "department": department
    }
    students.append(student)
    print("Student", name, "added successfully.")
    return True

def display_students():
    print("Student Records:")
    for student in students:
        print("Roll No:", student["roll_no"], " Name:", student["name"], " Department:", student["department"])

def search_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            return student
    print("Student not found.")
    return None

