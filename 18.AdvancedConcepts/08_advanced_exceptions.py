# 08_advanced_exceptions.py

class NegativeNumberError(Exception):
    pass


def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return num


try:
    value = int(input("Enter a number: "))
    print(check_number(value))
except NegativeNumberError as e:
    print("Custom Error:", e)
except ValueError:
    print("Invalid input")
finally:
    print("Execution completed")
