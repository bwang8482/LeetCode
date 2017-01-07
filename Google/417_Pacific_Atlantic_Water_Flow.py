"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

"""Solution:
"""


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        self.directions = [(-1,0), (1,0), (0,-1), (0,1)]
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.pacific = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.atlantic = [[False for _ in range(self.width)] for _ in range(self.height)]
        ans = []

        for x in range(self.width):
            self.dfs(0, x, self.pacific, matrix)
            self.dfs(self.height-1, x, self.atlantic, matrix)
        for y in range(self.height):
            self.dfs(y, 0, self.pacific, matrix)
            # Error 3: typo, right boundary is self.width - 1 
            self.dfs(y, self.width-1, self.atlantic, matrix)
        for j in range(self.height):
            for i in range(self.width):
                if self.atlantic[j][i] and self.pacific[j][i]:
                    ans.append([j, i])
        # Error 5: remember to return
        return ans

    # Error 2: remember to pass matrix
    def dfs(self, y, x, visited, matrix):
        visited[y][x] = True
        # Error 1: don't forget self.
        for direction in self.directions:
            i, j = x + direction[0], y + direction[1]
            # Error 4: remember to check visited!!!
            # Error 5: the condition: matrix[j][i] >= matrix[y][x]
            if 0 <= i < self.width and 0 <= j < self.height and not visited[j][i] and matrix[j][i] >= matrix[y][x]:
                self.dfs(j, i, visited, matrix)









