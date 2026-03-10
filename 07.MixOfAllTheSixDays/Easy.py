def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "Fail"


scores = []

n = int(input("Enter number of students: "))

for i in range(n):
    s = int(input("Enter score: "))
    scores.append(s)

print("\nStudent Results:")

for score in scores:
    grade = check_grade(score)
    print("Score:", score, "Grade:", grade)