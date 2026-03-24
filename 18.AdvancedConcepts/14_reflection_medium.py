# reflection_medium.py

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


def execute_operation(obj, method_name, a, b):

    # Check if method exists
    if hasattr(obj, method_name):

        method = getattr(obj, method_name)

        if callable(method):
            return method(a, b)
        else:
            return "Attribute is not callable"

    else:
        return "Invalid operation"


def main():
    calc = Calculator()

    print("Available operations: add, subtract, multiply, divide")

    operation = input("Enter operation: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = execute_operation(calc, operation, num1, num2)

    print("Result:", result)


main()
