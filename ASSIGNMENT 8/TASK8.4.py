# TASK 8.4: ShoppingCart Class Implementation

class ShoppingCart:
    """
    A shopping cart class that allows adding items, removing items,
    and calculating the total cost.
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}  # Dictionary: {item_name: price}
    
    def add_item(self, name, price):
        """
        Add an item to the cart.
        
        Args:
            name (str): Name of the item
            price (float): Price of the item
            
        Raises:
            ValueError: If name is empty or price is negative
            TypeError: If name is not a string or price is not a number
        """
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        if not name.strip():
            raise ValueError("Item name cannot be empty")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        self.items[name] = price
    
    def remove_item(self, name):
        """
        Remove an item from the cart.
        
        Args:
            name (str): Name of the item to remove
            
        Returns:
            bool: True if item was removed, False if item was not found
            
        Raises:
            TypeError: If name is not a string
        """
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        
        if name in self.items:
            del self.items[name]
            return True
        return False
    
    def total_cost(self):
        """
        Calculate the total cost of all items in the cart.
        
        Returns:
            float: Total cost of all items (0.0 if cart is empty)
        """
        return sum(self.items.values())


def _run_tests():
    """Run comprehensive test cases for ShoppingCart class."""
    
    print("Running ShoppingCart tests...")
    all_passed = True
    
    # Test 1: Initialize empty cart
    print("\n[Test 1] Initialize empty cart")
    cart1 = ShoppingCart()
    assert len(cart1.items) == 0, "Cart should be empty initially"
    assert cart1.total_cost() == 0.0, "Empty cart should have total cost 0.0"
    print("  ✓ PASS: Empty cart initialized correctly")
    
    # Test 2: Add single item
    print("\n[Test 2] Add single item")
    cart2 = ShoppingCart()
    cart2.add_item("Apple", 1.50)
    assert len(cart2.items) == 1, "Cart should have 1 item"
    assert cart2.items["Apple"] == 1.50, "Apple price should be 1.50"
    assert cart2.total_cost() == 1.50, "Total cost should be 1.50"
    print("  ✓ PASS: Single item added correctly")
    
    # Test 3: Add multiple items
    print("\n[Test 3] Add multiple items")
    cart3 = ShoppingCart()
    cart3.add_item("Apple", 1.50)
    cart3.add_item("Banana", 0.75)
    cart3.add_item("Orange", 2.00)
    assert len(cart3.items) == 3, "Cart should have 3 items"
    assert cart3.total_cost() == 4.25, "Total cost should be 4.25"
    print("  ✓ PASS: Multiple items added correctly")
    
    # Test 4: Add item with same name (overwrites)
    print("\n[Test 4] Add item with same name (overwrites)")
    cart4 = ShoppingCart()
    cart4.add_item("Apple", 1.50)
    cart4.add_item("Apple", 2.00)  # Overwrites previous price
    assert len(cart4.items) == 1, "Cart should still have 1 item"
    assert cart4.items["Apple"] == 2.00, "Apple price should be updated to 2.00"
    assert cart4.total_cost() == 2.00, "Total cost should be 2.00"
    print("  ✓ PASS: Item price overwritten correctly")
    
    # Test 5: Remove existing item
    print("\n[Test 5] Remove existing item")
    cart5 = ShoppingCart()
    cart5.add_item("Apple", 1.50)
    cart5.add_item("Banana", 0.75)
    result = cart5.remove_item("Apple")
    assert result is True, "remove_item should return True for existing item"
    assert len(cart5.items) == 1, "Cart should have 1 item after removal"
    assert "Apple" not in cart5.items, "Apple should be removed"
    assert cart5.total_cost() == 0.75, "Total cost should be 0.75"
    print("  ✓ PASS: Existing item removed correctly")
    
    # Test 6: Remove non-existent item
    print("\n[Test 6] Remove non-existent item")
    cart6 = ShoppingCart()
    cart6.add_item("Apple", 1.50)
    result = cart6.remove_item("Banana")
    assert result is False, "remove_item should return False for non-existent item"
    assert len(cart6.items) == 1, "Cart should still have 1 item"
    assert cart6.total_cost() == 1.50, "Total cost should remain 1.50"
    print("  ✓ PASS: Non-existent item removal handled correctly")
    
    # Test 7: Remove from empty cart
    print("\n[Test 7] Remove from empty cart")
    cart7 = ShoppingCart()
    result = cart7.remove_item("Apple")
    assert result is False, "remove_item should return False for empty cart"
    assert len(cart7.items) == 0, "Cart should remain empty"
    print("  ✓ PASS: Empty cart removal handled correctly")
    
    # Test 8: Total cost with various prices
    print("\n[Test 8] Total cost with various prices")
    cart8 = ShoppingCart()
    cart8.add_item("Item1", 10)
    cart8.add_item("Item2", 5.5)
    cart8.add_item("Item3", 0.25)
    cart8.add_item("Item4", 100.99)
    expected_total = 10 + 5.5 + 0.25 + 100.99
    assert abs(cart8.total_cost() - expected_total) < 0.01, f"Total should be {expected_total}"
    print(f"  ✓ PASS: Total cost calculated correctly: {cart8.total_cost()}")
    
    # Test 9: Add item with zero price
    print("\n[Test 9] Add item with zero price")
    cart9 = ShoppingCart()
    cart9.add_item("FreeItem", 0.0)
    assert cart9.items["FreeItem"] == 0.0, "Zero price should be allowed"
    assert cart9.total_cost() == 0.0, "Total cost should be 0.0"
    print("  ✓ PASS: Zero price item handled correctly")
    
    # Test 10: Invalid input - negative price
    print("\n[Test 10] Invalid input - negative price")
    cart10 = ShoppingCart()
    try:
        cart10.add_item("Item", -5.0)
        assert False, "Should raise ValueError for negative price"
    except ValueError as e:
        assert "negative" in str(e).lower(), "Error message should mention negative"
        print("  ✓ PASS: Negative price raises ValueError")
    
    # Test 11: Invalid input - empty name
    print("\n[Test 11] Invalid input - empty name")
    cart11 = ShoppingCart()
    try:
        cart11.add_item("", 5.0)
        assert False, "Should raise ValueError for empty name"
    except ValueError as e:
        assert "empty" in str(e).lower(), "Error message should mention empty"
        print("  ✓ PASS: Empty name raises ValueError")
    
    # Test 12: Invalid input - whitespace-only name
    print("\n[Test 12] Invalid input - whitespace-only name")
    cart12 = ShoppingCart()
    try:
        cart12.add_item("   ", 5.0)
        assert False, "Should raise ValueError for whitespace-only name"
    except ValueError:
        print("  ✓ PASS: Whitespace-only name raises ValueError")
    
    # Test 13: Invalid input - non-string name
    print("\n[Test 13] Invalid input - non-string name")
    cart13 = ShoppingCart()
    try:
        cart13.add_item(123, 5.0)
        assert False, "Should raise TypeError for non-string name"
    except TypeError as e:
        assert "string" in str(e).lower(), "Error message should mention string"
        print("  ✓ PASS: Non-string name raises TypeError")
    
    # Test 14: Invalid input - non-numeric price
    print("\n[Test 14] Invalid input - non-numeric price")
    cart14 = ShoppingCart()
    try:
        cart14.add_item("Item", "five")
        assert False, "Should raise TypeError for non-numeric price"
    except TypeError as e:
        assert "number" in str(e).lower(), "Error message should mention number"
        print("  ✓ PASS: Non-numeric price raises TypeError")
    
    # Test 15: Invalid input - remove_item with non-string
    print("\n[Test 15] Invalid input - remove_item with non-string")
    cart15 = ShoppingCart()
    cart15.add_item("Apple", 1.50)
    try:
        cart15.remove_item(123)
        assert False, "Should raise TypeError for non-string name in remove_item"
    except TypeError:
        print("  ✓ PASS: Non-string name in remove_item raises TypeError")
    
    # Test 16: Complex scenario - add, remove, add again
    print("\n[Test 16] Complex scenario - add, remove, add again")
    cart16 = ShoppingCart()
    cart16.add_item("Apple", 1.50)
    cart16.add_item("Banana", 0.75)
    cart16.remove_item("Apple")
    cart16.add_item("Apple", 2.00)  # Add again with different price
    assert cart16.items["Apple"] == 2.00, "Apple should have new price"
    assert cart16.total_cost() == 2.75, "Total should be 2.75"
    print("  ✓ PASS: Complex add/remove/add scenario works correctly")
    
    # Test 17: Remove all items
    print("\n[Test 17] Remove all items")
    cart17 = ShoppingCart()
    cart17.add_item("Item1", 10.0)
    cart17.add_item("Item2", 20.0)
    cart17.remove_item("Item1")
    cart17.remove_item("Item2")
    assert len(cart17.items) == 0, "Cart should be empty"
    assert cart17.total_cost() == 0.0, "Total cost should be 0.0"
    print("  ✓ PASS: All items removed correctly")
    
    print("\n" + "="*50)
    print("All ShoppingCart tests PASSED!")
    print("="*50)


if __name__ == "__main__":
    _run_tests()
    print("\nFull class with tested functionalities")
