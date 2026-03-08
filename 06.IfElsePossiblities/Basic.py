# Program demonstrating basic conditional statements

number = int(input("Enter a number: "))

# Simple IF
if number > 0:
    print("The number is positive")

# IF - ELSE
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# IF - ELIF - ELSE
if number > 100:
    print("Number is greater than 100")
elif number > 50:
    print("Number is between 51 and 100")
elif number > 10:
    print("Number is between 11 and 50")
else:
    print("Number is 10 or less")

# Multiple IF statements
if number % 3 == 0:
    print("Divisible by 3")

if number % 5 == 0:
    print("Divisible by 5")
