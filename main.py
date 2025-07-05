from part1.randomized_select import randomized_select
from part1.deterministic_select import deterministic_select
from part2.array import Array
from part2.stack import Stack
from part2.queue import Queue
from part2.linked_list import LinkedList

# Part 1 test
arr = [7, 2, 1, 10, 5, 3, 8]
k = 3
print("Randomized Select:", randomized_select(arr.copy(), 0, len(arr) - 1, k))
print("Deterministic Select:", deterministic_select(arr.copy(), k))

# Part 2 test
print("\nArray test:")
a = Array()
a.insert(10)
a.insert(20)
a.delete(10)
print(a.data)

print("\nStack test:")
s = Stack()
s.push(1)
s.push(2)
print(s.pop())

print("\nQueue test:")
q = Queue()
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())

print("\nLinked List test:")
ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.traverse()
ll.delete(10)
ll.traverse()
