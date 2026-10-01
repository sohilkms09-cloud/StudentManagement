import student

def show():
    print("1. Add Student")
    print("2. Display Student Details")
    print("3. Search for a student")

def main():
    while True:
        show()
        try:
            choice = int(input("Enter Choice (1/2/3): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if choice == 1:
            print("Add a Student")
            roll_no = int(input("Enter a roll number: "))
            name = input("Enter a Name: ")
            department = input("Enter a department: ")
            student.add_student(roll_no, name, department)
            
        elif choice == 2:
            student.display_students()  
        elif choice == 3:
            roll_no = int(input("Enter a roll number for search: "))
            print(student.search_student(roll_no))
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

