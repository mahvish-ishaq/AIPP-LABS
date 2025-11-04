# Task 4: Calculate sum of first n natural numbers using different looping techniques

def sum_to_n_for(n):
    """Sum of first n numbers using FOR loop"""
    total = 0  # Initialize total to 0
    # Loop through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        total += i  # Add current number to total
    print(f"Sum of first {n} numbers using for loop = {total}")


def sum_to_n_while(n):
    """Sum of first n numbers using WHILE loop"""
    total = 0  # Initialize total to 0
    i = 1      # Start counter from 1
    # Continue the loop until i exceeds n
    while i <= n:
        total += i  # Add i to total
        i += 1      # Increment i by 1
    print(f"Sum of first {n} numbers using while loop = {total}")


# Taking input from user
num = int(input("Enter a number: "))

# Call both functions to calculate sum
sum_to_n_for(num)
sum_to_n_while(num)

# Another approach — Using mathematical formula
# Formula for sum of first n natural numbers = n * (n + 1) / 2
formula_sum = num * (num + 1) // 2  # Using integer division for exact result
print(f"Sum using formula = {formula_sum}")
