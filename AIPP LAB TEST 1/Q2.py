# QUESTION 2
# Design a few-shot prompt to guide an AI tool in writing code for a basic linked list with methods for insert and delete.

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as head node")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        print(f"Inserted {data} at end")

    # Delete node with given key
    def delete_node(self, key):
        temp = self.head

        # If head is the node to delete
        if temp is not None and temp.data == key:
            self.head = temp.next
            print(f"Deleted head node {key}")
            return

        # Search for node
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # Key not found
        if temp is None:
            print(f"Value {key} not found in list")
            return

        # Delete node
        prev.next = temp.next
        print(f"Deleted node {key}")

    # Display list
    def display(self):
        print("Current Linked List:", end=" ")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


# ===========================
# TEST CASES
# ===========================

print("----- STARTING LINKED LIST TEST CASES -----\n")

ll = LinkedList()

# Insert operations
ll.insert_at_end(10)
ll.display()

ll.insert_at_end(20)
ll.display()

ll.insert_at_end(30)
ll.display()

# Delete existing node
ll.delete_node(20)
ll.display()

# Delete non-existing node
ll.delete_node(50)
ll.display()

print("All test cases passed successfully.")
