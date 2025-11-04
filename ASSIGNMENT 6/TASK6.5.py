# Task 5: Create a BankAccount class with deposit, withdraw, and balance methods

# Step 1: Define a class named BankAccount
class BankAccount:
    # Constructor initializes account holder name and balance
    def __init__(self, account_holder, balance=0):
        # 'self' refers to the current object instance
        self.account_holder = account_holder   # Name of account holder
        self.balance = balance                 # Initial account balance (default = 0)

    # Step 2: Define method to deposit money
    def deposit(self, amount):
        """Add amount to balance"""
        # Check if entered amount is positive
        if amount > 0:
            self.balance += amount  # Update balance
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive!")  # Handle invalid input

    # Step 3: Define method to withdraw money
    def withdraw(self, amount):
        """Withdraw amount if sufficient balance"""
        # Validate withdrawal amount
        if amount <= 0:
            print("Invalid withdrawal amount.")
        # If user tries to withdraw more than balance
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            # Deduct from balance
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

    # Step 4: Define method to display current balance
    def display_balance(self):
        """Display current balance"""
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")


# Step 5: Take input from the user
name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

# Step 6: Create an object of BankAccount class
account = BankAccount(name, initial_balance)

# Step 7: Create a menu-driven banking system for user interaction
while True:
    print("\n---- BANK MENU ----")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    # Step 8: Take user’s choice
    choice = input("Enter your choice: ")

    # Step 9: Perform operations based on user choice
    if choice == '1':
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)        # Call deposit method
    elif choice == '2':
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)       # Call withdraw method
    elif choice == '3':
        account.display_balance()   # Call display method
    elif choice == '4':
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice! Try again.")
