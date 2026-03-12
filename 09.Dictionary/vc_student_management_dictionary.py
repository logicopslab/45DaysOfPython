# Very Complex Program: Student Management System

students = {}


def add_student():

    name = input("Enter student name: ")
    marks_input = input("Enter marks separated by space: ")

    marks = []

    for m in marks_input.split():
        marks.append(int(m))

    students[name] = {
        "marks": marks
    }


def calculate_average(marks):

    total = 0

    for m in marks:
        total += m

    return total / len(marks)


def display_students():

    print("\nStudent Records")

    for name, data in students.items():

        marks = data["marks"]
        avg = calculate_average(marks)

        print(name, "Marks:", marks, "Average:", avg)


def find_topper():

    highest = 0
    topper = ""

    for name, data in students.items():

        marks = data["marks"]
        avg = calculate_average(marks)

        if avg > highest:
            highest = avg
            topper = name

    print("Topper:", topper, "Average:", highest)


def class_statistics():

    all_marks = []

    for data in students.values():

        for m in data["marks"]:
            all_marks.append(m)

    print("First 5 marks:", all_marks[:5])
    print("Last 5 marks:", all_marks[-5:])


while True:

    print("\n1 Add Student")
    print("2 Display Students")
    print("3 Find Topper")
    print("4 Class Statistics")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        find_topper()

    elif choice == 4:
        class_statistics()

    elif choice == 5:
        break

    else:
        print("Invalid option")
