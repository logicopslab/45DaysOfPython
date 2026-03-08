# Function to convert age from string to integer
def convert_age(age_str):
    return int(age_str)


# Function to convert height from string to float
def convert_height(height_str):
    return float(height_str)


# Function to calculate BMI
def calculate_bmi(weight_str, height):
    weight = float(weight_str)  # convert string to float
    bmi = weight / (height ** 2)
    return bmi


# Function to categorize BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Main function controlling the program flow
def main():
    name = input("Enter your name: ")
    age_input = input("Enter your age: ")
    height_input = input("Enter height in meters: ")
    weight_input = input("Enter weight in kg: ")

    age = convert_age(age_input)
    height = convert_height(height_input)

    bmi = calculate_bmi(weight_input, height)

    category = bmi_category(bmi)

    print("\nHealth Report")
    print("Name:", str(name))
    print("Age:", str(age))
    print("BMI:", str(round(bmi, 2)))
    print("Category:", category)


# Program starts here
main()
