'''TASK 5'''
# Write Code to Calculate Sum of ODD number and EVEN numbers in the list.
# Later Refactor the code written with improved logic.

def sum_even_odd(nums):
    even_sum = sum(x for x in nums if x % 2 == 0)
    odd_sum = sum(x for x in nums if x % 2 != 0)
    return even_sum, odd_sum
def sum_even_odd(nums):
    even_sum = sum(x for x in nums if x % 2 == 0)
    odd_sum = sum(x for x in nums if x % 2 != 0)
    return even_sum, odd_sum

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_sum, odd_sum = sum_even_odd(numbers)
#numbers = [1,2,3,4,5,6]
even_sum, odd_sum = sum_even_odd(numbers)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

# REFACTORED VERSION OF THIS ABOVE CODE
# TASK 5 - Refactored: single-pass computation, minimal functions

from typing import Iterable, List, Tuple

def sum_even_odd(nums: Iterable[int]) -> Tuple[int, int]:
    """Compute sums of even and odd integers in a single pass (O(n))."""
    even = 0
    odd = 0
    for x in nums:
        if x & 1 == 0:   # bitwise check slightly faster than x % 2 == 0
            even += x
        else:
            odd += x
    return even, odd

def parse_input_to_ints(s: str) -> List[int]:
    """Parse a space-separated string into a list of ints (may raise ValueError)."""
    return [int(p) for p in s.split() if p]

if __name__ == "__main__":
    s = input("Enter integers separated by spaces (press Enter to quit): ").strip()
    if not s:
        print("Exiting.")
    else:
        try:
            nums = parse_input_to_ints(s)
            even_sum, odd_sum = sum_even_odd(nums)
            print("Sum of even numbers:", even_sum)
            print("Sum of odd numbers:", odd_sum)
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")