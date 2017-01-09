"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


"""Solution:
    1. for each point, if the point is not visited, using dfs to search for the longest decreasing path
    2. store the value in dp array
    3. for each point, find the max length of smaller neighbor from dp
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # Error 1: remember to check null!
        if not matrix or not matrix[0]: return 0
        height = len(matrix)
        width = len(matrix[0])
        # initialize the dp array
        dp = [[0 for x in range(width)] for y in range(height)]
        ans = 0
        # dfs to calculate the longest decreasing path
        def dfs(j, i):
            if dp[j][i] == 0:
                # dfs on four neighbors
                left = dfs(j, i-1) if i-1 >= 0 and matrix[j][i] > matrix[j][i-1] else 0
                right = dfs(j, i+1) if i+1 < width and matrix[j][i] > matrix[j][i+1] else 0
                top = dfs(j-1, i) if j-1 >= 0 and matrix[j][i] > matrix[j-1][i] else 0
                bottom = dfs(j+1, i) if j+1 < height and matrix[j][i] > matrix[j+1][i] else 0
                # add 1 for itself
                dp[j][i] = 1 + max(left, right, top, bottom)
            return dp[j][i]
        # find the longest path
        for j in range(height):
            for i in range(width):
                ans = max(ans, dfs(j, i))
        return ans



        









