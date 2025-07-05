import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    rest = arr[:pivot_index] + arr[pivot_index+1:]
    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

# Example usage
if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Original:", data)
    print("Sorted:", randomized_quicksort(data))

