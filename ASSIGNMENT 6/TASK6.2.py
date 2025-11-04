# Program to print first 10 multiples of a number using loops

def print_multiples_for(num):
    """Print first 10 multiples using for loop"""
    print(f"\nFirst 10 multiples of {num} (using for loop):")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def print_multiples_while(num):
    """Print first 10 multiples using while loop"""
    print(f"\nFirst 10 multiples of {num} (using while loop):")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

# Taking input
n = int(input("Enter a number: "))
print_multiples_for(n)
print_multiples_while(n)
