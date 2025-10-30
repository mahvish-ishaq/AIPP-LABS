'''TASK 4'''
# Install and configure Cursor AI. Use it to generate a Python function (e.g., sum of squares). 
# WE DO IT USING VS CODE AI INTEGRATION WITH GITHUB COPILOT ONLY FOR NOW (INSTEAD OF CURSOR AI).
# ...existing code...

from typing import Iterable

def sum_of_squares(nums: Iterable[float]) -> float:
    """Return the sum of squares of the numbers in nums."""
    return sum(x * x for x in nums)

def prompt_numbers(prompt: str) -> list[float]:
    """
    Prompt the user to enter numbers separated by commas.
    Returns a list of floats. If the user enters empty input or 'exit', returns an empty list.
    """
    while True:
        s = input(prompt).strip()
        if s == "" or s.lower() in ("exit", "quit", "q"):
            return []
        parts = [p.strip() for p in s.split(",") if p.strip() != ""]
        try:
            return [float(p) for p in parts]
        except ValueError:
            print("Invalid input. Enter numbers separated by commas (e.g. 1, 2.5, 3) or 'exit' to quit.")

if __name__ == "__main__":
    print("Sum of squares calculator. Enter numbers separated by commas, or press Enter/type 'exit' to quit.")
    while True:
        nums = prompt_numbers("Numbers: ")
        if not nums:
            print("Exiting.")
            break
        print(f"sum_of_squares({nums}) = {sum_of_squares(nums)}")
