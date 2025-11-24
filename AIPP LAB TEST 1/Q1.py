# QUESTION - 1 
# Create a function to reverse a list in Python.Test and compare the performance of each version.

import timeit

# ------------------------------
# 1. Manual method (insert at front)
# ------------------------------
def reverse_manual(lst):
    reversed_list = []
    for item in lst:
        reversed_list.insert(0, item)
    return reversed_list


# ------------------------------
# 2. Using slicing
# ------------------------------
def reverse_slice(lst):
    return lst[::-1]


# ------------------------------
# 3. Using built-in reverse() - in place
# ------------------------------
def reverse_builtin(lst):
    lst.reverse()
    return lst


# ------------------------------
# 4. Using reversed() function
# ------------------------------
def reverse_reversed(lst):
    return list(reversed(lst))


# ------------------------------
# 5. Two-pointer swapping
# ------------------------------
def reverse_two_pointer(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst


# --------------------------------------------------------------
# TESTING ALL FUNCTIONS
# --------------------------------------------------------------

sample_list = [1, 2, 3, 4, 5]

print("Original:", sample_list)

print("Manual:", reverse_manual(sample_list))
print("Slice:", reverse_slice(sample_list))
print("Built-in:", reverse_builtin(sample_list[:]))  # use copy
print("Reversed():", reverse_reversed(sample_list))
print("Two-pointer:", reverse_two_pointer(sample_list[:]))

# --------------------------------------------------------------
# PERFORMANCE COMPARISON USING timeit
# --------------------------------------------------------------

big_list = list(range(10000))

print("\n--- Performance Comparison (Lower time = Faster) ---")

print("Manual (insert at front):",
      timeit.timeit(lambda: reverse_manual(big_list), number=100))

print("Slicing [::-1]:",
      timeit.timeit(lambda: reverse_slice(big_list), number=100))

print("Built-in reverse():",
      timeit.timeit(lambda: reverse_builtin(big_list[:]), number=100))

print("reversed():",
      timeit.timeit(lambda: reverse_reversed(big_list), number=100))

print("Two-pointer swapping:",
      timeit.timeit(lambda: reverse_two_pointer(big_list[:]), number=100))
