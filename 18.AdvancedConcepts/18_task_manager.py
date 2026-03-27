# task_manager.py

tasks = []


def add_task(task):
    tasks.append(task)
    print("Task added successfully")


def view_tasks():
    if not tasks:
        print("No tasks available")
        return

    print("\nYour Tasks:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")


def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number")


def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)

        elif choice == "4":
            print("Exiting program")
            break

        else:
            print("Invalid choice")


main()
