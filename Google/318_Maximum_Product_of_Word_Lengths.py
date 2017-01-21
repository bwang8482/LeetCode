"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""

"""Solution:
    1. represent each word as a binary number with 26 bits, stands for a-z.
    2. if the AND of two binary number is 0, those two numbers have no common letter
    3. sort the word by length and calculate the max length from the longest word
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        binary_words = collections.defaultdict(int)
        for word in words:
            binary_word = 0
            # Tip: using set() to avoid duplicated letter
            for char in set(word):
                # Error 1: use ord() to transfer str to int
                binary_word |= 1 << ord(char)-ord('a')
            binary_words[binary_word] = max(binary_words.get(binary_word, 0), len(word))
        # Tip: using 'or [0]' to handle the situation when previous list is empty
        return max([binary_words[i] * binary_words[j] for i in binary_words for j in binary_words if not i & j] or [0])











