"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


"""Solution:
    1. this problem can be solved by backtracking
    2. track the number of '(' not used
    3. track the number of ')' can use
    4. for each step, choose '(' or ')'
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        self.backtracking('', 2*n, n, 0)
        return self.ans

    def backtracking(self, string, length, prefix, suffix):
        if length <= 0:
            self.ans.append(string)
            return
        if prefix > 0:
            self.backtracking(string + '(', length-1, prefix-1, suffix+1)
        if suffix > 0:
            self.backtracking(string + ')', length-1, prefix, suffix-1)
        return


"""Summary:
    this is a typical backtracking problem.
"""





