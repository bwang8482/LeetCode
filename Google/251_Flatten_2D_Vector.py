"""
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Hint:

1. How many variables do you need to keep track?
2. Two variables is all you need. Try with x and y.
3. Beware of empty rows. It could be the first few rows.
4. To write correct code, think about the invariant to maintain. What is it?
5. The invariant is x and y must always point to a valid point in the 2d vector. Should you maintain your invariant ahead of time or right when you need it?
6. Not sure? Think about how you would implement hasNext(). Which is more complex?
7. Common logic in two different places should be refactored into a common method.
"""


"""Solution:
    1. using two pointer x,y to track the 2d vector
    2. moving x in next()
    3. checking new line in hasNext(), because there are may be empty rows.
"""


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.x = 0
        self.y = 0


    def next(self):
        """
        :rtype: int
        """
        ret = self.vec2d[self.y][self.x]
        self.x += 1
        return ret


    def hasNext(self):
        """
        :rtype: bool
        """
        # tip: check newline in hasNext()
        while self.y < len(self.vec2d):
            if self.x < len(self.vec2d[self.y]):
                return True
            self.y += 1
            self.x = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

"""Summary:
    1. for iterator problem, checking validation in hasNext()
    2. return True in narrow conditions and return False in common case
"""





