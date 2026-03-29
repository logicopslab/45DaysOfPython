# inventory_system.py

inventory = {}


def add_item(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
    print(f"{name} added/updated successfully")


def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"{name} removed")
    else:
        print("Item not found")


def update_item(name, quantity):
    if name in inventory:
        inventory[name] = quantity
        print(f"{name} updated")
    else:
        print("Item not found")


def view_inventory():
    if not inventory:
        print("Inventory is empty")
        return

    print("\nInventory:")
    for item, qty in inventory.items():
        print(f"{item}: {qty}")


def main():
    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            add_item(name, qty)

        elif choice == "2":
            name = input("Enter item name: ")
            remove_item(name)

        elif choice == "3":
            name = input("Enter item name: ")
            qty = int(input("Enter new quantity: "))
            update_item(name, qty)

        elif choice == "4":
            view_inventory()

        elif choice == "5":
            print("Exiting system")
            break

        else:
            print("Invalid choice")


main()
