"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

"""Solution:
    1. add new number as new set
    2. union new set with neighbor
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) is 0 or len(grid[0]) is 0:
            return 0
        self.island = Union()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.island.add((i,j))
                    # Error 1: remember to unite
                    for near in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                        if near in self.island.rank:
                            self.island.unite(near, (i,j))
        return self.island.count

class Union(object):
    def __init__(self):
        # Tip: this is rank
        self.rank = {}
        self.id = {}
        self.count = 0

    def add(self, index):
        if index not in self.id:
            self.rank[index] = 1
            self.id[index] = index
            self.count += 1

    def root(self, index):
        # Tip: this is path compression
        while self.id[index] != index:
            self.id[index] = self.id[self.id[index]]
            index = self.id[index]
        return index

    def unite(self, left, right):
        root_left, root_right = self.root(left), self.root(right)
        if root_left == root_right:
            return
        if root_right > root_left:
            root_left, root_right = root_right, root_left
        self.id[root_right] = root_left
        self.rank[root_left] += self.rank[root_right]
        self.count -= 1




