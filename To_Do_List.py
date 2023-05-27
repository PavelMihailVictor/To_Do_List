class TodoItem:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def mark_item_completed(self, index):
        if 0 <= index < len(self.items):
            self.items[index].mark_completed()
        else:
            print("Invalid item index.")

    def display_items(self):
        if not self.items:
            print("No items in the to-do list.")
        else:
            print("To-Do List:")
            for index, item in enumerate(self.items):
                status = "✓" if item.completed else "◻"
                print(f"{index}. [{status}] {item.title}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Item")
        print("2. Mark Item as Completed")
        print("3. Display Items")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the item title: ")
            item = TodoItem(title)
            todo_list.add_item(item)
            print("Item added successfully!")
        elif choice == "2":
            index = int(input("Enter the item index to mark as completed: "))
            todo_list.mark_item_completed(index)
        elif choice == "3":
            todo_list.display_items()
        elif choice == "4":
            print("Exiting To-Do List...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
