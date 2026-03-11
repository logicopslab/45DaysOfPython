# Complex Program: Student marks management using lists

def add_student(students):
    name = input("Enter student name: ")
    marks_input = input("Enter marks separated by space: ")

    marks = []
    for m in marks_input.split():
        marks.append(int(m))

    students.append([name, marks])


def display_students(students):

    print("\nStudent Records")

    for i in range(len(students)):
        name = students[i][0]
        marks = students[i][1]

        total = 0
        for m in marks:
            total += m

        average = total / len(marks)

        print(i + 1, name, "Marks:", marks, "Average:", average)


def highest_average(students):

    highest = 0
    topper = ""

    for student in students:

        name = student[0]
        marks = student[1]

        total = 0
        for m in marks:
            total += m

        avg = total / len(marks)

        if avg > highest:
            highest = avg
            topper = name

    print("Topper:", topper, "Average:", highest)


def main():

    students = []

    while True:

        print("\n1 Add Student")
        print("2 Display Students")
        print("3 Find Topper")
        print("4 Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student(students)

        elif choice == 2:
            display_students(students)

        elif choice == 3:
            highest_average(students)

        elif choice == 4:
            break

        else:
            print("Invalid option")


main()