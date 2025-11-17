# TASK 2 - Queue Implementation

class Queue:
    """Queue implemented using Python list."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add element to the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return front element."""
        if self.is_empty():
            return "Queue is empty!"
        return self.items.pop(0)

    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0


# ----- User Menu -----
q = Queue()

while True:
    print("\n--- Queue Operations Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Check if Empty")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter an element to enqueue: ")
        q.enqueue(item)
        print(f"{item} added to the queue.")

    elif choice == "2":
        print("Dequeued:", q.dequeue())

    elif choice == "3":
        print("Is queue empty?", q.is_empty())

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
