# Function definition
def calculate_area(length, width):
    area = length * width
    return area

# User input
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Function call
result = calculate_area(length, width)

# Output
print("Area of the rectangle is:", result)
