"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

"""Solution:

"""

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.child = 0
        self.queue = []
        self.total = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.child == self.size:
            self.total -= self.queue.pop(0)
            self.child -= 1
        self.total += val
        self.child += 1
        self.queue.append(val)
        return float(self.total)/float(self.child)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)