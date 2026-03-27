# student_record_system.py

def add_students():
    students = {}

    n = int(input("Enter number of students: "))

    for _ in range(n):
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks

    return students


def display_sorted(students):
    print("\nStudents sorted by marks (highest first):")

    sorted_students = sorted(
        students.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for name, marks in sorted_students:
        print(f"{name}: {marks}")


def find_topper(students):
    topper = max(students, key=students.get)
    print("\nTopper:", topper, "-", students[topper])


def main():
    students = add_students()

    display_sorted(students)
    find_topper(students)


main()
