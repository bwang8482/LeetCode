"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""

"""Solution:
    1. this problem can be solved by backtracing.
    2. iterating all possible next moves and return False if no move available.
    3. if the there if next moves that return False, return True
    4. this problem can be optimized by memorization.
"""

class Solution(object):
    _memo = {}
    # function to check win
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s not in self._memo:
            self._memo[s] = False
            for move in self.next(s):
                if self.canWin(move) == False:
                    self._memo[s] = True
        return self._memo[s]
    # function to calculate all posible next moves
    def next(self, s):
        ret = []
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                ret.append(s[:i] + '-' + s[i+2:])
        return ret


