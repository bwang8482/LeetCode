"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
"""


"""Solution:
    1. this problem could be solved by recursion
    2. for each recursion function, if length is smaller than n
    3. adding strobogrammatic word to both left and right sides
    4. choose different start states for even and odd n
"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Tip: return [""] for n = 0
        if n == 0: return [""]
        # initialize start states
        self.size = n
        self.dict = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        self.ans = []
        string = []
        # different start states for odd and even
        if self.size % 2:
            string = ['0','1','8']
        else:
            string = ['']
        left, right = 0, self.size-1
        # calling recursion function
        for substring in string:
            self.recursion(left, right, substring)
        return self.ans

    def recursion(self, left, right, string):
        # if length is n, return
        if left >= right:
            # Error 1: the starting digit cannot be 0 except when n = 1
            if (string == '') or (len(string) != 1 and string[0] == '0'):
                return 
            self.ans.append(string)
            return
        else:
            for key in self.dict:
                self.recursion(left+1, right-1, key + string + self.dict[key])
