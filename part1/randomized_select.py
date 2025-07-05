import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    q = partition(arr, low, high)
    length = q - low + 1
    if k == length:
        return arr[q]
    elif k < length:
        return randomized_select(arr, low, q - 1, k)
    else:
        return randomized_select(arr, q + 1, high, k - length)
