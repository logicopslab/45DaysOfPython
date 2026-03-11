# Easy Program: Calculate sum and average of numbers in a list

numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)