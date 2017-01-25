"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


"""Solution: dfs -- Time Limit Exceeded
    1. start from left upper corner
    2. move downward if number in next row is smaller than target
    3. otherwise, move right
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.ans = False
        self.dfs(0, 0, target)
        return self.ans

    def dfs(self, i, j, target):
        if i >= self.height or j >= self.width:
            return
        if self.matrix[i][j] == target:
            self.ans = True
        elif self.matrix[i][j] < target:
            self.dfs(i+1, j, target)
            self.dfs(i, j+1, target)
        return
"""Summary:
    dfs need too much redundant traversing.
"""



"""Solution: iteration
    1. using iteration to traverse
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        height, width, i, j = len(matrix), len(matrix[0]), 0, 0
        while True:
            if i < 0 or j >= width:
                return False
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            elif i+1 >= height or matrix[i+1][j] > target:
                j += 1
            else:
                i += 1
"""Summary:
    return True when find target or return False when beyond boundary.    
"""









