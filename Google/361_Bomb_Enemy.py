"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) is 0 or len(grid[0]) is 0:
            return
        dp = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        ans = 0
        # left
        for i in range(len(grid)):
            kill = 0
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    dp[i][j] += kill
                elif grid[i][j] == 'E':
                    kill += 1
                elif grid[i][j] == 'W':
                    kill = 0
        # right
        for i in range(len(grid)):
            kill = 0
            for j in range(len(grid[0])-1,-1,-1):
                if grid[i][j] == '0':
                    dp[i][j] += kill
                elif grid[i][j] == 'E':
                    kill += 1
                elif grid[i][j] == 'W':
                    kill = 0
        # top
        for j in range(len(grid[0])):
            kill = 0
            for i in range(len(grid)):
                if grid[i][j] == '0':
                    dp[i][j] += kill
                elif grid[i][j] == 'E':
                    kill += 1
                elif grid[i][j] == 'W':
                    kill = 0
        # bottom
        for j in range(len(grid[0])):
            kill = 0
            for i in range(len(grid)-1,-1,-1):
                if grid[i][j] == '0':
                    dp[i][j] += kill
                    # Error 1: remember to return
                    if dp[i][j] > ans:
                        ans = dp[i][j]
                elif grid[i][j] == 'E':
                    kill += 1
                elif grid[i][j] == 'W':
                    kill = 0
        return ans