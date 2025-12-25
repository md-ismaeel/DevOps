students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Student Grade")
    print("3. Display All Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # add student
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully.")

    # update student
    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            new_grade = input("Enter new grade: ")
            students[name] = new_grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")
    # display all
    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(name, ":", grade)
    # exit
    elif choice == "4":
        print("Exiting program.")
        break
    # invalid
    else:
        print("Invalid choice. Please try again.")
