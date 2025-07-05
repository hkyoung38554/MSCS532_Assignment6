# MSCS532 Assignment 6: Medians and Order Statistics and Elementary Data Structures

This project implements and analyzes two selection algorithms to find the k-th smallest element in an array. It also includes basic data structure implementations such as arrays, stacks, queues, and linked lists.

## Files

### Part 1 – Selection Algorithms

- part1/randomized_select.py: Expected linear time randomized selection (Quickselect)
- part1/deterministic_select.py: Worst-case linear time deterministic selection (Median of Medians)

### Part 2 – Elementary Data Structures

- part2/array.py: Array with insert, delete, and access methods
- part2/stack.py: Stack implemented using list (LIFO)
- part2/queue.py: Queue implemented using list (FIFO)
- part2/linked_list.py: Singly linked list with insert, delete, and traverse

### Other Files

- main.py: Test script for all algorithms and data structures
- Assignment6_Haeri Kyoung.pdf: Final report with implementation details, analysis, and findings
- README.md: This file

## How to Run

To test all functionality:

python main.py

## Summary

- Selection Algorithms: Compared deterministic and randomized methods for selecting the k-th smallest element. Both were correct and efficient, with Quickselect faster in practice and Median of Medians more stable.
- Data Structures: Built from scratch to understand internal logic, performance, and use cases.

This assignment reinforced concepts in algorithm design and core data structures with hands-on implementation and performance analysis.

