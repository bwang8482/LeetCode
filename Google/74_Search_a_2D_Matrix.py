"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
"""

"""Solution:
    1. This question can be solved by binary search.
    2. we can convert the 2d index into 1d and use binary search on 1d index
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        row = len(matrix)
        col = len(matrix[0])
        # Error 1: typo, right should be row * col
        left, right = 0, row*col - 1
        # binary search
        while left <= right:
            # using this instead of (left+right)/2 to avoid overflow
            mid = left + (right - left)/2
            # convert 1d index to 2d
            val = matrix[mid/col][mid%col]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False



