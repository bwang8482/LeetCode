"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


"""Solution:
    1. this problem can be solved by classified discussion.
    2. for 4 different directions, pop the matrix from different ends
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction = 0
        ans = []
        while matrix and matrix[0]:
            # from left to right
            if direction == 0:
                ans += matrix.pop(0)
                direction = 1
            # from top to bottom
            elif direction == 1:
                for row in matrix:
                    ans.append(row.pop())
                direction = 2
            # from right to left
            elif direction == 2:
                ans += matrix.pop()[::-1]
                direction = 3
            # from bottom to top
            else:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
                    direction = 0
        return ans

"""Summary:
    this problem can be solved by simply classified discussion.
If I cannot modified original matrix, I can use 4 boundaries for traversing.
"""









