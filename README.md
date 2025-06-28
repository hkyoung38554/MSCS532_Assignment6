# MSCS532 Assignment5: Quicksort Algorithm: Implementation, Analysis, and Randomization

This project implements both deterministic and randomized versions of the Quicksort algorithm. It includes a detailed analysis of their time and space complexities, empirical performance comparisons on different input distributions, and a discussion of how randomization helps avoid worst-case behavior.

## Files

- `quicksort_deterministic.py`: Python implementation of standard Quicksort using the last element as pivot  
- `quicksort_randomized.py`: Randomized Quicksort that selects the pivot randomly in each recursive call  
- `quicksort_comparison.py`: Benchmark script comparing deterministic and randomized Quicksort on random, sorted, and reverse-sorted inputs  
- `Assignment5_Haeri Kyoung.pdf`: Final report discussing implementation choices, complexity analysis, and experimental results  
- `README.md`: Instructions and summary of the project  

## How to Run

```bash
python quicksort_deterministic.py
python quicksort_randomized.py
python quicksort_comparison.py
```

## Summary of Findings

### Deterministic Quicksort

- Selected the last element as pivot, leading to unbalanced partitions on sorted or reverse-sorted data.
- Time complexity was order n log n in the best and average cases but degraded to order n squared in the worst case.
- Performance dropped significantly on already sorted or reverse-sorted lists, confirming theoretical expectations.

### Randomized Quicksort

- Randomly selected pivot helped avoid worst-case input patterns.
- Achieved consistent average-case time complexity of order n log n across all input types.
- More robust than deterministic version with better real-world performance on unpredictable data.

### Empirical Comparison

- Randomized Quicksort consistently outperformed the deterministic version on non-random inputs.
- Runtime measurements supported theoretical claims, showing stable behavior across increasing input sizes and data distributions.
- Reinforced the value of pivot randomization as a simple but effective optimization.
