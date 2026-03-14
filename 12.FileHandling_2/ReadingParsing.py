# Student record management using files

def add_student():

    file = open("students.txt", "a")

    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    file.write(name + "," + marks + "\n")

    file.close()


def display_students():

    file = open("students.txt", "r")

    print("\nStudent Records")

    for line in file:
        data = line.strip().split(",")

        name = data[0]
        marks = data[1]

        print("Name:", name, "Marks:", marks)

    file.close()


while True:

    print("\n1 Add Student")
    print("2 Display Students")
    print("3 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        break

    else:
        print("Invalid option")
