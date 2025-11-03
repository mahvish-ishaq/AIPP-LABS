def fib(n):
    """Return the nth Fibonacci number using recursion"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Example
print(f"FIBONACCI NUMBER IS:{fib(6)}")

'''This function directly follows the Fibonacci definition:
F(n) = F(n-1) + F(n-2)
It repeatedly calls itself until it reaches the base cases n=0 or n=1.
Each call computes smaller Fibonacci numbers, but it recomputes the same values many times.'''

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(f"FIBONACCI NUMBER IS:{fib(10)}")
'''
@lru_cache automatically stores results of previous calls.
So when fib(3) is needed again, it’s retrieved from memory instead of recalculated.
This eliminates redundant work and makes the function very fast.'''