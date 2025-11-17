#TASK 4 - Binary Search Tree Implementation

class BSTNode:
    """Node for Binary Search Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Simple BST implementation."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert value into BST."""
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert(node.right, value)

    def inorder_traversal(self):
        """Return sorted values (inorder traversal)."""
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)


# ------------------ MENU SYSTEM ------------------

bst = BinarySearchTree()

while True:
    print("\n--- Binary Search Tree Operations Menu ---")
    print("1. Insert Value")
    print("2. Display Inorder Traversal")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        val = int(input("Enter value to insert into BST: "))
        bst.insert(val)
        print(f"{val} inserted into BST.")

    elif choice == "2":
        print("Inorder Traversal (Sorted):", bst.inorder_traversal())

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
