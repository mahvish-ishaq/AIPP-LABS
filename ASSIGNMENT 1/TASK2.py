# USE COPILOT TO GENERATE A IS_PRIME FUNCTION.
import math
def is_prime(n):
    """
    Checks if a given integer n is a prime number.
    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.
    """
    if n <= 1:
        return False

    # Check for divisibility from 2 up to the square root of n.
    # If n has a divisor greater than its square root, it must have a
    # corresponding divisor smaller than its square root, which would have
    # already been found.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # Found a divisor, so it's not prime

    return True  # No divisors found, so it is prime


if __name__ == "__main__":
    for _ in range(5): # Loop 5 times
        try:
            s = input("Enter an integer: ").strip()
            if s == "":
                print("No input provided.")
            else:
                n = int(s)
                if is_prime(n):
                    print(f"{n} is prime")
                else:
                    print(f"{n} is not prime")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
