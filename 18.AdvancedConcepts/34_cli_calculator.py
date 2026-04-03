# cli_calculator.py

import argparse


def calculate(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")

    parser.add_argument("operation", help="Operation: add, sub, mul, div")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")

    args = parser.parse_args()

    result = calculate(args.operation, args.a, args.b)

    print("Result:", result)


if __name__ == "__main__":
    main()
