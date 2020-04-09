#!/usr/bin/env python
"""
Min Max Stack Construction
  Design a Min Max stack that supports
  Pushing and popping values on and off the stack.
  Peeking at the value at the top of the stack.
  Getting both the minimum and the maximum values in the stack at any given
point in time.
  All operations should run in a constant time.

var minMaxStack = Stack<Int>()
minMaxStack.push(5)
minMaxStack.getMax()
-> returns 5
minMaxStack.getMin()
-> returns 5
minMaxStack.push(2)
minMaxStack.getMax()
-> returns 5
minMaxStack.getMin()
-> returns 2
minMaxStack.push(20)
minMaxStack.getMax()
-> returns 20
minMaxStack.getMin()
-> returns 2
minMaxStack.peek()
-> returns 20
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self): # constructor - how to start up the object
        self.top = None
        self.length = 0
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    def push(self, value):
        if self.isEmpty():
            self.top = Node(value)
        else:
            new_top = Node(value)
            new_top.next = self.top
            self.top = new_top
        self.length += 1
    def peek(self):
        if self.isEmpty():
            return None
        return self.top.value
    def pop(self):
        if self.isEmpty():
            return None
            
        top_value = self.top.value
        self.top = self.top.next
        self.length -= 1
        return top_value

class StackStats:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        assert max >= min, f"StackStats: {max} < {min}!"

class MinMaxStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.stats = Stack()
    def push(self, value):
        if self.isEmpty():
            self.stats.push(StackStats(value, value))
        else:
            self.stats.push(StackStats(
                min = min(self.getMin(), value),
                max = max(self.getMax(), value)
            ))
        Stack.push(self, value)
    def pop(self):
        self.stats.pop()
        return Stack.pop(self)
    def getMax(self):
        return self.stats.top.value.max
    def getMin(self):
        return self.stats.top.value.min
        
        
import random
if __name__ == "__main__":
    
    min_max_stack = MinMaxStack()
    for i in range(10):
        min_max_stack.push(random.randint(1,10))
        print(f"peek: {min_max_stack.peek()}, min: {min_max_stack.getMin()}, max: {min_max_stack.getMax()}")
    while not min_max_stack.isEmpty():
        print(f"pop: {min_max_stack.pop()}, min: {min_max_stack.getMin()}, max: {min_max_stack.getMax()}")
    #print(f"min: {min_max_Stack.getMin()}")"









