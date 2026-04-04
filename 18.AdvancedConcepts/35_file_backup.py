# file_backup.py

import os
import shutil


def backup_files(source, destination):
    if not os.path.exists(source):
        print("Source folder does not exist")
        return

    if not os.path.exists(destination):
        os.makedirs(destination)

    files = os.listdir(source)

    for file in files:
        src_path = os.path.join(source, file)
        dest_path = os.path.join(destination, file)

        if os.path.isfile(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"Copied: {file}")


def main():
    source = input("Enter source directory: ")
    destination = input("Enter backup directory: ")

    backup_files(source, destination)


main()
