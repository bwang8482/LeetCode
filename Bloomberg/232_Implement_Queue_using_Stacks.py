"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

"""
Solution:
1. two stack: in_stack and out_stack
2. one for push and one for pop
3. if out_stack is empty, move all elements from in_stack to out_stack
"""

"""
Error:
1. syntax for list empty(): using 'not list'
2. syntax for and: not &&, but (not self.in_stack) and (not self.out_stack)
"""

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.in_stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        if self.empty():
        	return None
        return self.out_stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        if self.empty():
        	return None
        return self.out_stack[-1]

        

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.in_stack) and (not self.out_stack)

    def move(self):
    	"""
    	:rtype: nothing
    	"""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())






