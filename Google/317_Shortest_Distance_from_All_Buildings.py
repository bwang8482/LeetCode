"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
"""

"""Solution:
    # 1. traverse every available space
    # 2. calculate the distance with BFS
    # 3. choose the space with smallest distance
    1. start from building with 1
    2. traverse all empty node
    3. calculate the distance to node
"""

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) is 0 or len(grid[0]) is 0:
            return -1
        
        self.height = len(grid)
        self.width = len(grid[0])
        self.start = []
        self.
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == 1:
                    self.start.append((i, j))

        def BFS(x, y):
            queue = collections.deque([x, y, 0])
            visit = [[False]*self.width for _ in range(self.height)]
            while queue:
                x, y, distance = queue.popleft()

                for j,i in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0 <= i < self.height and 0 <= j < self.width and not visit[i][j]:
                        queue.append([j,i,distance+1])
                        visit[i][j] = True





















