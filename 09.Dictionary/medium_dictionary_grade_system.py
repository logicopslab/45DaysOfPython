# Medium Program: Assign grades using dictionary data

def get_grade(score):

    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "Fail"


students = {}

n = int(input("Number of students: "))

for i in range(n):
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    students[name] = score


print("\nStudent Grades")

for name, score in students.items():
    grade = get_grade(score)
    print(name, "Score:", score, "Grade:", grade)
