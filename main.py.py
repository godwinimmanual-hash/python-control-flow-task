# main.py

from utils import add_item, remove_item, display_items


def main():
    items = []

    while True:
        print("\n===== LIST MANAGER =====")
        print("1. Add Item")
        print("2. View Items")
        print("3. Delete Item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_item(items)

        elif choice == "2":
            display_items(items)

        elif choice == "3":
            remove_item(items)

        elif choice == "4":
            print("Thank you for using List Manager!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()