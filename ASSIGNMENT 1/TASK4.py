# FACTORIAL FUNCTION PROGRAM
def factorial_recursive(n: int) -> int:
    """Return n! using recursion. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("factorial undefined for negative values")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n: int) -> int:
    """Return n! using an iterative approach. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("factorial undefined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def prompt_non_negative_integer(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        if s == "":
            print("No input provided. Please enter a non-negative integer.")
            continue
        try:
            n = int(s)
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    MIN_ENTRIES = 2

    while True:
        for i in range(1, MIN_ENTRIES + 1):
            n = prompt_non_negative_integer(f"Enter non-negative integer #{i}: ")
            print(f"Recursive: {n}! = {factorial_recursive(n)}")# function that calls itself within its own definition.
            print(f"Iterative: {n}! = {factorial_iterative(n)}")# Using loops (like for or while) to repeat a block of code a certain number of times or until a condition is met.

        cont = input("Do you want to enter more numbers? (y/n): ").strip().lower()
        if cont not in ("y", "yes"):
            print("Exiting.")
            break
