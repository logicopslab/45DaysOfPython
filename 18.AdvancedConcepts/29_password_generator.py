# password_generator.py

import random
import string


def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += "!@#$%^&*()"

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    length = int(input("Enter password length: "))
    digits = input("Include digits? (y/n): ").lower() == "y"
    special = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_password(length, digits, special)

    print("Generated Password:", password)


main()
