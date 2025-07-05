class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        temp = self.head
        if temp and temp.value == value:
            self.head = temp.next
            return
        prev = None
        while temp and temp.value != value:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print("None")
