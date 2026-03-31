# simple_logger.py

from datetime import datetime


LOG_FILE = "app.log"


def write_log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {level} - {message}\n"

    with open(LOG_FILE, "a") as file:
        file.write(log_entry)


def info(message):
    write_log("INFO", message)


def warning(message):
    write_log("WARNING", message)


def error(message):
    write_log("ERROR", message)


def main():
    while True:
        print("\n1. Info Log")
        print("2. Warning Log")
        print("3. Error Log")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            msg = input("Enter info message: ")
            info(msg)

        elif choice == "2":
            msg = input("Enter warning message: ")
            warning(msg)

        elif choice == "3":
            msg = input("Enter error message: ")
            error(msg)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


main()
