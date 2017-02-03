"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


"""Solution:
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        self.ans = []
        self.maps = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.bfs('', digits)
        return self.ans

    def bfs(self, string, digits):
        if not digits:
            self.ans.append(string)
            return
        for char in self.maps[digits[0]]:
            self.bfs(string + char, digits[1:])
            
        







