# Complex Python Program Demonstrating All Loop Types

students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [60, 70, 65],
    "David": [45, 50, 40],
    "Eva": []
}

print("----- Student Grade Processing System -----\n")

# 1. FOR LOOP over dictionary
for student, grades in students.items():

    print(f"\nProcessing student: {student}")

    # PASS example: placeholder for missing grades
    if not grades:
        print("No grades available yet.")
        pass
        continue

    total = 0

    # 2. NESTED FOR LOOP (processing grades)
    for index, grade in enumerate(grades):

        # CONTINUE example
        if grade < 0:
            print("Invalid grade found, skipping")
            continue

        print(f"Exam {index+1} score:", grade)
        total += grade

        # BREAK example
        if grade == 100:
            print("Perfect score detected. Stopping grade scan.")
            break

    average = total / len(grades)

    print("Average:", average)

    # classification
    if average >= 90:
        print("Performance: Excellent")
    elif average >= 75:
        print("Performance: Good")
    elif average >= 60:
        print("Performance: Average")
    else:
        print("Performance: Needs Improvement")

else:
    # FOR-ELSE example
    print("\nFinished processing all students.\n")


# 3. WHILE LOOP Example
print("----- Searching for a Student With Average > 90 -----")

student_names = list(students.keys())
i = 0

while i < len(student_names):

    name = student_names[i]
    grades = students[name]

    if not grades:
        i += 1
        continue

    avg = sum(grades) / len(grades)

    print(f"Checking {name}, average = {avg}")

    if avg > 90:
        print("High performing student found:", name)
        break

    i += 1

else:
    # WHILE-ELSE example
    print("No student found with average greater than 90.")


# 4. More Complex Nested Loop (multiplication table example)
print("\n----- Multiplication Table (Nested Loop Example) -----")

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()


print("\nProgram execution completed.")
