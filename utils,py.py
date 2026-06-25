# utils.py

def add_item(items):
    """Add an item to the list."""
    item = input("Enter item to add: ").strip()

    if item:
        items.append(item)
        print(f"'{item}' added successfully.")
    else:
        print("Item cannot be empty.")


def remove_item(items):
    """Remove an item from the list."""
    if not items:
        print("The list is empty. Nothing to remove.")
        return

    display_items(items)

    item = input("Enter item to remove: ").strip()

    if item in items:
        items.remove(item)
        print(f"'{item}' removed successfully.")
    else:
        print("Item not found in the list.")


def display_items(items):
    """Display all items in the list."""
    if not items:
        print("\nThe list is empty.\n")
    else:
        print("\nCurrent List:")
        print("-" * 20)
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item}")
        print("-" * 20)