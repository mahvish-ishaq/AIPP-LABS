# TASK 2 - BUBBLE SORT ALGORITHM

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

data = [5, 1, 4, 2, 8]
print("Sorted:", bubble_sort(data))
