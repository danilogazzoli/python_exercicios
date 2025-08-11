# -*- coding: utf-8 -*-
'''
Stack works on the principle of “Last-in, first-out” LIFO. 
Also, the inbuilt functions in Python make the code short and simple. 
To add an item to the top of the list, i.e., to push an item, 
we use append() function and to pop out an element we use pop() function. 
These functions work quiet efficiently and fast in end operations.
'''

# Python code to demonstrate Implementing
# stack using list
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack)

# Removes the last item
print(stack.pop())

print(stack)

# Removes the last item
print(stack.pop())

print(stack)

# Peek (look at the top element)
if stack:
    print("Top element:", stack[-1])

'''
Queue works on the principle of “First-in, first-out”. FIFO
Below is list implementation of queue. We use pop(0) to remove the first item from a list.
'''

queue = ['laranja','maçã','morango']
print(queue)
queue.append('uva')
print(queue)
queue.append('limão')
print(queue)

print(queue.pop(0))
print(queue)

print('*'*100)

queue.remove('maçã')
print(queue)

queue.insert(2, 'maçã')
print(queue)

queue2 = ['pera','abacaxi']
queue.extend(queue2)
print(queue)

queue.sort()
print(queue)
print(queue.index('morango'))

queue.pop(queue.index('morango'))
print(queue)


# 2. Stack using collections.deque
# Better performance for large stacks because .append() and .pop() are O(1).

from collections import deque

stack = deque()

stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushes:", stack)

print("Popped:", stack.pop())
print("Stack after pop:", stack)

# 3. Stack as a Class (Encapsulation)
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Usage
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Top element:", s.peek())
print("Popped:", s.pop())
print("Is empty?", s.is_empty())

