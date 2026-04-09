# file_integrity_checker.py

import hashlib


def calculate_hash(file_name):
    hasher = hashlib.sha256()

    try:
        with open(file_name, "rb") as file:
            while chunk := file.read(4096):
                hasher.update(chunk)

        return hasher.hexdigest()

    except FileNotFoundError:
        print("File not found")
        return None


def verify_file(file_name, original_hash):
    current_hash = calculate_hash(file_name)

    if current_hash is None:
        return

    print("Original Hash:", original_hash)
    print("Current Hash :", current_hash)

    if current_hash == original_hash:
        print("File is unchanged (Integrity OK)")
    else:
        print("File has been modified!")


def main():
    file_name = input("Enter file name: ")

    print("\nGenerate original hash first:")
    original_hash = calculate_hash(file_name)

    if original_hash:
        print("Saved Hash:", original_hash)

        input("\nModify the file if you want, then press Enter...")

        verify_file(file_name, original_hash)


main()
