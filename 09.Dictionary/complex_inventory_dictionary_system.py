# Complex Program: Inventory management using dictionaries

inventory = {}


def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    inventory[name] = {
        "price": price,
        "quantity": quantity
    }


def display_inventory():

    print("\nInventory List")

    for product, details in inventory.items():
        print(product,
              "Price:", details["price"],
              "Quantity:", details["quantity"])


def update_quantity():
    name = input("Enter product name to update: ")

    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name]["quantity"] = qty
    else:
        print("Product not found")


while True:

    print("\n1 Add Product")
    print("2 Display Inventory")
    print("3 Update Quantity")
    print("4 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_product()

    elif choice == 2:
        display_inventory()

    elif choice == 3:
        update_quantity()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
