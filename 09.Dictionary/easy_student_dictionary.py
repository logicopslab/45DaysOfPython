# Easy Program: Store and display student marks using a dictionary

students = {}

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Records")

for name in students:
    print(name, ":", students[name])
