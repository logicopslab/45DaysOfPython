# Very Complex Program: Multi-class student analysis

classes = {}

num_classes = int(input("Enter number of classes: "))

for i in range(num_classes):
    class_name = input("Enter class name: ")
    students = set(input("Enter students separated by space: ").split())
    classes[class_name] = students

print("\n--- Class Data ---")
for name, students in classes.items():
    print(name, ":", students)

# Find students in ALL classes
common_students = None

for students in classes.values():
    if common_students is None:
        common_students = students
    else:
        common_students = common_students.intersection(students)

print("\nStudents present in all classes:", common_students)

# Find all unique students
all_students = set()

for students in classes.values():
    all_students = all_students.union(students)

print("All unique students:", all_students)

# Find students unique to each class
print("\nUnique students per class:")

for name, students in classes.items():

    others = set()

    for other_name, other_students in classes.items():
        if name != other_name:
            others = others.union(other_students)

    unique_students = students.difference(others)

    print(name, "unique students:", unique_students)
