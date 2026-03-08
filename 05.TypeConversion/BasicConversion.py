# Function to convert input strings to integers
def convert_to_int(num1, num2):
    a = int(num1)
    b = int(num2)
    return a, b


# Function to add numbers
def add_numbers(a, b):
    return a + b


# Main program
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

a, b = convert_to_int(num1, num2)

result = add_numbers(a, b)

# Convert result to string for output formatting
print("The sum is: " + str(result))
