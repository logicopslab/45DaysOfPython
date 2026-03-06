def get_student_data():
    students = {}
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks
    
    return students


def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


def calculate_average(students):
    total = sum(students.values())
    return total / len(students)


def display_results(students):
    print("\nStudent Results")
    print("----------------")
    
    for name, marks in students.items():
        grade = calculate_grade(marks)
        print(name, "Marks:", marks, "Grade:", grade)


def main():
    students = get_student_data()
    display_results(students)
    
    avg = calculate_average(students)
    print("\nClass Average:", avg)


# Program execution starts here
main()
