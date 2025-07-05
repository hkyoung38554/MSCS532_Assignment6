<<<<<<< HEAD
# MSCS532 Assignment 6: Medians and Order Statistics & Elementary Data Structures

This project implements and analyzes selection algorithms (Randomized and Deterministic) for finding the k-th smallest element in an array. It also includes basic data structure implementations such as arrays, stacks, queues, and linked lists. The project explores both theoretical complexity and practical performance.

## Files

### Part 1 – Selection Algorithms

- `part1/randomized_select.py`: Expected linear time randomized selection using Quickselect
- `part1/deterministic_select.py`: Worst-case linear time deterministic selection using Median of Medians

### Part 2 – Elementary Data Structures

- `part2/array.py`: Array implementation with insert, delete, and access operations
- `part2/stack.py`: Stack implemented using a Python list (LIFO)
- `part2/queue.py`: Queue implemented using a Python list (FIFO)
- `part2/linked_list.py`: Singly linked list with insert, delete, and traversal operations

### Supporting Files

- `main.py`: Test script demonstrating all core functionalities
- `Assignment6_Haeri Kyoung.pdf`: Final written report including implementation details, complexity analysis, and results
- `README.md`: Instructions and summary of the project
=======
# MSCS532 Assignment5: Quicksort Algorithm: Implementation, Analysis, and Randomization

This project implements both deterministic and randomized versions of the Quicksort algorithm. It includes a detailed analysis of their time and space complexities, empirical performance comparisons on different input distributions, and a discussion of how randomization helps avoid worst-case behavior.

## Files

- `quicksort_deterministic.py`: Python implementation of standard Quicksort using the last element as pivot  
- `quicksort_randomized.py`: Randomized Quicksort that selects the pivot randomly in each recursive call  
- `quicksort_comparison.py`: Benchmark script comparing deterministic and randomized Quicksort on random, sorted, and reverse-sorted inputs  
- `Assignment5_Haeri Kyoung.pdf`: Final report discussing implementation choices, complexity analysis, and experimental results  
- `README.md`: Instructions and summary of the project  
>>>>>>> 7d0321ede56174402e0e72af82a33472e9970d9b

## How to Run

```bash
<<<<<<< HEAD
python main.py
```

This will run all test cases for both selection algorithms and data structures.

## Summary of Findings

### Selection Algorithms

- **Randomized Select**: Achieved expected time complexity of order n. Performed well in practice but showed slight variability based on input order due to randomness.
- **Deterministic Select**: Achieved true linear time in worst-case. More consistent but slightly slower in smaller datasets due to overhead of extra steps (grouping, median selection).
- Both methods correctly handled arrays with duplicate elements and various sizes.

### Elementary Data Structures

- **Array**: Provided constant-time access and efficient insert/delete for unsorted data. Ideal for random access-heavy use cases.
- **Stack & Queue**: Both operated as expected with push/pop and enqueue/dequeue. Stack used list append/pop, while queue removed from the front.
- **Linked List**: Allowed efficient insertion and deletion at the head. Traversal demonstrated correct pointer linking.

---

This assignment helped me better understand the trade-offs between different selection strategies and solidified my grasp of how fundamental data structures are built from scratch. It also strengthened my ability to evaluate performance based on both theory and observation.
=======
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
>>>>>>> 7d0321ede56174402e0e72af82a33472e9970d9b
