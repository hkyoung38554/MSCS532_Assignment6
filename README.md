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

## How to Run

```bash
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
