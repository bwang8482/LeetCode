"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
"""

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) is 0 or len(matrix[0]) is 0:
            return
        self.row = len(matrix)
        self.col = len(matrix[0])
        # Error 1: initialize 2d array
        self.nums = [[0 for x in range(self.col)] for y in range(self.row)]
        self.tree = [[0 for x in range(self.col + 1)] for y in range(self.row + 1)]
        for j in range(self.row):
            for i in range(self.col):
                self.update(j, i, matrix[j][i])        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        val -= self.nums[row][col]
        self.nums[row][col] += val
        y = row + 1
        while y < self.row + 1:
            # Error 1: x = row + 1 TYPO!!
            x = col + 1
            while x < self.col + 1:
                self.tree[y][x] += val
                x += x & (-x)
            y += y & (-y)

        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Error 2: check the boundary!!!
        return self.sum(row2, col2) + self.sum(row1-1, col1-1) - self.sum(row1-1, col2) - self.sum(row2, col1-1)
        

    def sum(self, row, col):
        total = 0
        y = row + 1
        while y:
            x = col + 1
            while x:
                total += self.tree[y][x]
                x -= x & (-x)
            y -= y & (-y)
        return total

        

# Your NumMatrix object will be instantiated and called as such:
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
numMatrix = NumMatrix(matrix)
print numMatrix.nums
print numMatrix.tree
print numMatrix.sumRegion(2, 1, 4, 3)

numMatrix.update(3, 2, 2)
print numMatrix.nums
print numMatrix.sumRegion(2, 1, 4, 3)

