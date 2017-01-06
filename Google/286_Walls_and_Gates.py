"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

"""Solution:
    1. traverse rooms and push the gates into queue
    2. using bfs to set depth for neighbors
"""

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        queue = collections.deque()
        height = len(rooms)
        width = len(rooms[0])
        visited = [[False for x in range(width)] for y in range(height)]
        # push gates and set visited
        for j in range(height):
            for i in range(width):
                if rooms[j][i] == 0:
                    queue.append((i, j, 0))
                    visited[j][i] = True
                elif rooms[j][i] == -1:
                    visited[j][i] = True
        # bfs
        while queue:
            x, y, depth = queue.popleft()
            if rooms[y][x] == 2147483647:
                rooms[y][x] = depth
            for i,j in (x+1,y), (x-1,y), (x,y+1), (x,y-1):
                if 0 <= i < width and 0 <= j < height and not visited[j][i]:
                    # Error 1: using i, j not x, y (typo)
                    queue.append((i, j, depth+1))
                    visited[j][i] = True










