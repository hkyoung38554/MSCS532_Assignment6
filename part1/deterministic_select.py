def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k - 1]
    
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    pivot = deterministic_select(medians, len(medians)//2 + 1)

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k <= len(low):
        return deterministic_select(low, k)
    elif k > len(low) + len(equal):
        return deterministic_select(high, k - len(low) - len(equal))
    else:
        return pivot
