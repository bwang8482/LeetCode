"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""

"""Solution
1. reverse all element before adding new one
"""

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # using collections.deque() instead of list
        # list has no popleft() function
        self.queue = collections.deque()
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        for i in range(self.size):
            self.queue.append(self.queue.popleft())
        self.size += 1       

    def pop(self):
        """
        :rtype: nothing
        """
        if self.size == 0:
            return
        self.size -= 1
        self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0




