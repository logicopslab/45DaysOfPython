# undo_redo_system.py

undo_stack = []
redo_stack = []
current_state = ""


def perform_action(action):
    global current_state

    undo_stack.append(current_state)
    current_state += action
    redo_stack.clear()

    print("Current State:", current_state)


def undo():
    global current_state

    if undo_stack:
        redo_stack.append(current_state)
        current_state = undo_stack.pop()
        print("Undo →", current_state)
    else:
        print("Nothing to undo")


def redo():
    global current_state

    if redo_stack:
        undo_stack.append(current_state)
        current_state = redo_stack.pop()
        print("Redo →", current_state)
    else:
        print("Nothing to redo")


def main():
    while True:
        print("\n1. Add Text")
        print("2. Undo")
        print("3. Redo")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            text = input("Enter text: ")
            perform_action(text)

        elif choice == "2":
            undo()

        elif choice == "3":
            redo()

        elif choice == "4":
            break

        else:
            print("Invalid choice")


main()
