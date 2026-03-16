
# Very Complex Program: Employee record analysis using tuples

employees = []

n = int(input("Enter number of employees: "))

for i in range(n):

    name = input("Enter employee name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    employee = (name, age, salary)
    employees.append(employee)


print("\nEmployee Records")
for emp in employees:
    print(emp)


# Find highest salary
highest_salary = 0
highest_employee = None

for emp in employees:
    if emp[2] > highest_salary:
        highest_salary = emp[2]
        highest_employee = emp

print("\nHighest Paid Employee:", highest_employee)


# Average salary
total_salary = 0

for emp in employees:
    total_salary += emp[2]

average_salary = total_salary / len(employees)

print("Average Salary:", average_salary)


# Sort employees by salary
sorted_employees = sorted(employees, key=lambda x: x[2])

print("\nEmployees sorted by salary:")
for emp in sorted_employees:
    print(emp)
