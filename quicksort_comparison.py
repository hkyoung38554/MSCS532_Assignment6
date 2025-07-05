import time
import random
from quicksort_deterministic import quicksort
from quicksort_randomized import randomized_quicksort

def generate_data(size, mode="random"):
    if mode == "sorted":
        return list(range(size))
    elif mode == "reversed":
        return list(range(size, 0, -1))
    else:
        return [random.randint(0, size) for _ in range(size)]

def test(sort_func, data):
    start = time.time()
    sort_func(data.copy())
    return round(time.time() - start, 6)

if __name__ == "__main__":
    sizes = [1000, 5000, 10000]
    modes = ["random", "sorted", "reversed"]

    for mode in modes:
        print(f"\nInput Type: {mode}")
        for size in sizes:
            data = generate_data(size, mode)
            t1 = test(quicksort, data)
            t2 = test(randomized_quicksort, data)
            print(f"Size: {size} | Deterministic: {t1}s | Randomized: {t2}s")
