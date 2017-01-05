"""
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:
Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.

Explanation:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6 
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example:
Given m = 1, n = 1, return 9.
"""

"""Solution:
    1. for this question, I will use dfs.
    2. first we need to build a skip array to handle the skip situation
    3. second, we will pruning the symetric positions
    4. for each start point, call dfs on its possible next moves
    5. return the number for each length in m to n
"""

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # using skip array to check skip
        self.skip = [[0 for j in range(10)] for i in range(10)]
        self.skip[1][3] = self.skip[3][1] = 2
        self.skip[1][7] = self.skip[7][1] = 4
        self.skip[3][9] = self.skip[9][3] = 6
        self.skip[7][9] = self.skip[9][7] = 8
        self.skip[1][9] = self.skip[9][1] = self.skip[3][7] = self.skip[7][3] = self.skip[2][8] = self.skip[8][2] = self.skip[4][6] = self.skip[6][4] = 5
        
        self.ans = 0
        self.visited = [False for i in range(10)]
        # pruning for symetric position
        for i in range(m, n+1):
            self.ans += self.dfs(1,i-1) * 4
            self.ans += self.dfs(2,i-1) * 4
            self.ans += self.dfs(5,i-1)
        return self.ans

    def dfs(self, cur, remain):
        if remain == 0:
            return 1
        self.visited[cur] = True
        rst = 0
        # Error 1: traverse from 1 to 9 not from 0.
        for i in range(1,10):
            # Error 2: use visited as boolen table not set.
            if not self.visited[i] and (self.skip[cur][i] == 0 or self.visited[self.skip[cur][i]]):
                rst += self.dfs(i, remain-1)
        self.visited[cur] = False
        return rst

         






