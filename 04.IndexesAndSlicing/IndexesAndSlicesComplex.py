# List of student names
students = ["John", "Emma", "Liam", "Olivia", "Noah"]

# Corresponding marks
marks = [78, 92, 85, 69, 95]

# Print all students with marks using indexes
print("Student Scores")
for i in range(len(students)):
    print("Index:", i, "| Name:", students[i], "| Marks:", marks[i])


# Find the topper using indexes
highest_index = 0

for i in range(len(marks)):
    if marks[i] > marks[highest_index]:
        highest_index = i

print("\nTopper of the class:")
print(students[highest_index], "with marks", marks[highest_index])


# Increase marks of a specific student using index search
search_name = input("\nEnter student name to give bonus marks: ")

for i in range(len(students)):
    if students[i] == search_name:
        marks[i] += 5
        print("Updated marks for", students[i], ":", marks[i])
        break


# Demonstrate slicing using indexes
print("\nFirst three students:", students[0:3])
print("Last two students:", students[-2:])
