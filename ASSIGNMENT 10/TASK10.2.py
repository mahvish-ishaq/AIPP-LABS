# TASK 2 – Optimize Redundant Loops
def find_common(a, b):
    return list(set(a) & set(b))

# ----- User Input -----
list1 = input("Enter first list (comma-separated): ").split(",")
list2 = input("Enter second list (comma-separated): ").split(",")

# Remove spaces
list1 = [x.strip() for x in list1]
list2 = [x.strip() for x in list2]

# ----- Output -----
print("Common elements:", find_common(list1, list2))
