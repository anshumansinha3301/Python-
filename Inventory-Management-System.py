class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = InventoryItem(name, quantity)
        print(f"Added {quantity} of {name} to inventory.")

    def remove_item(self, name, quantity):
        if name in self.items:
            if self.items[name].quantity >= quantity:
                self.items[name].quantity -= quantity
                print(f"Removed {quantity} of {name} from inventory.")
                if self.items[name].quantity == 0:
                    del self.items[name]
                    print(f"{name} removed from inventory as quantity is zero.")
            else:
                print(f"Cannot remove {quantity} of {name}. Only {self.items[name].quantity} available.")
        else:
            print(f"{name} not found in inventory.")

    def view_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item in self.items.values():
                print(item)

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            inventory.add_item(name, quantity)

        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity to remove: "))
            inventory.remove_item(name, quantity)

        elif choice == '3':
            inventory.view_inventory()

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
