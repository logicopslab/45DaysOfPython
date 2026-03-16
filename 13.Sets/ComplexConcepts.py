# Complex Program: Student course analysis

python_students = set(input("Students in Python course: ").split())
java_students = set(input("Students in Java course: ").split())

both_courses = python_students.intersection(java_students)
all_students = python_students.union(java_students)
only_python = python_students.difference(java_students)
only_java = java_students.difference(python_students)

print("\nStudents in both courses:", both_courses)
print("All enrolled students:", all_students)
print("Only Python students:", only_python)
print("Only Java students:", only_java)

print("\nTotal Python students:", len(python_students))
print("Total Java students:", len(java_students))
