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
