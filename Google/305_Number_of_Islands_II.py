"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]
"""

"""Solution:
    1. using find-union: disjoint-set algorithm
    2. add new set when adding new position
    3. unite the new set with all its neighbor
"""

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        land = Union()
        for position in positions:
            # Error 1: remember to convert list to tuple
            land.add(tuple(position))
            for x,y in (-1, 0), (1, 0), (0, -1), (0, 1):
                neighbor = (position[0] + x, position[1] + y)
                if neighbor in land.id:
                    land.unite(tuple(position), neighbor)
            ans.append(land.island)
        return ans


class Union(object):
    def __init__(self):
        self.rank = {}
        self.id = {}
        self.island = 0

    def root(self, index):
        while self.id[index] != index:
            self.id[index] = self.id[self.id[index]]
            index = self.id[index]
        return index

    def add(self, index):
        # Error 2: remember to check duplicate
        if index not in self.id:
            self.rank[index] = 1
            self.id[index] = index
            self.island += 1

    def unite(self, left, right):
        root_left, root_right = self.root(left), self.root(right)
        if root_left == root_right:
            return
        if self.rank[root_right] > self.rank[root_left]:
            root_left, root_right = root_right, root_left
        self.id[root_right] = root_left
        self.rank[root_left] += self.rank[root_right]
        self.island -= 1















