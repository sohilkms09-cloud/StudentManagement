while True:
    show()

    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        student.add_student(roll_no, name, department)

    elif choice == 2:
        student.display_students()

    elif choice == 3:
        roll_no = int(input("Enter Roll Number to search: "))
        student.search_student(roll_no)

    elif choice == 4:
        roll_no = int(input("Enter Roll Number to delete: "))
        student.delete_student(roll_no)

    elif choice == 5:
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")

