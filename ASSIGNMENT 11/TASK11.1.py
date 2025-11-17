#TASK 1 - Stack Class Implementation
class Stack:
    """Simple Stack implementation using Python list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop()

    def peek(self):
        """Return top item without removing it."""
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0


# ---------- Menu Driven Program ----------
s = Stack()

while True:
    print("\n----- STACK OPERATIONS -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter value to push: ")
        s.push(item)
        print(f"{item} pushed onto stack.")

    elif choice == "2":
        print("Popped:", s.pop())

    elif choice == "3":
        print("Top element:", s.peek())

    elif choice == "4":
        print("Is stack empty?", s.is_empty())

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
