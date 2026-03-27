# password_checker.py

def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = "!@#$%^&*()_+"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    score = sum([has_upper, has_lower, has_digit, has_special])

    if len(password) < 6:
        return "Weak (too short)"
    elif score == 4 and len(password) >= 8:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"


def main():
    password = input("Enter password: ")
    result = check_password_strength(password)
    print("Password Strength:", result)


main()
