# Medium Program: Store and display student information using tuples

student = ("Alice", 20, "Computer Science", 88)

print("Student Tuple:", student)

name = student[0]
age = student[1]
course = student[2]
marks = student[3]

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)

# Tuple unpacking
name, age, course, marks = student

print("\nUsing unpacking:")
print(name, age, course, marks)
