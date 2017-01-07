"""
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""

"""Solution:
    1. this question can be solved by backtracking
    2. iterating through the word, for each char, choose to abbreviate or ignore.
"""


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.size = len(word)
        self.ans = []
        self.backtracking(word, 0, "", 0)
        return self.ans
    
    def backtracking(self, word, pointer, string, count):
        if pointer == self.size:
            if count > 0:
                string += str(count)
            self.ans.append(string)
        else:
            # abbreviate current char
            self.backtracking(word, pointer+1, string, count+1)
            # ignore the current char
            if count > 0:
                string += str(count)
            string += word[pointer]
            self.backtracking(word, pointer+1, string, 0)














