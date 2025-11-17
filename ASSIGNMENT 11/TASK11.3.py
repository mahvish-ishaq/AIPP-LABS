# TASK 3 -  Linked List Implementation

class Node:
    """Node class for Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the start."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        """Display all nodes."""
        if self.head is None:
            print("Linked List is empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------- MENU ----------
ll = LinkedList()

while True:
    print("\n--- Linked List Operations Menu ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Display List")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        data = input("Enter value to insert at beginning: ")
        ll.insert_at_beginning(data)
        print(f"{data} inserted at beginning.")

    elif choice == "2":
        data = input("Enter value to insert at end: ")
        ll.insert_at_end(data)
        print(f"{data} inserted at end.")

    elif choice == "3":
        print("Linked List:")
        ll.display()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option! Please choose between 1-4.")
