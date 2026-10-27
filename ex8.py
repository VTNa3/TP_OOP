students = []

while True:
    print("\nChoose a choice: 1.Add 2.Show 3.Exit")
    choice = int(input("Choose: "))

    match choice:
        case 1:
            name = input("Name: ")
            if name != "":
                students.append(name)
                print("Student added successfully!")
            else:
                print("Name cannot be empty!")

        case 2:
            print(students)

        case 3:
            print("Exit program")
            break

        case _:
            print("Invalid choice!")