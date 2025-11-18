# TASK 1 - LINEAR SEARCH IMPLEMENTATION
def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

arr = [3, 5, 7, 1, 9]
value = 7
print("Index:", linear_search(arr, value))
