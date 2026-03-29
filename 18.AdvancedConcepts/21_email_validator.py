# email_validator.py

import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def check_email(email):
    if is_valid_email(email):
        return "Valid Email"
    else:
        return "Invalid Email"


def main():
    email = input("Enter email: ")
    result = check_email(email)
    print(result)


main()
