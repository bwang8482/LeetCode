"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

"""Solution:
    1. two pointer, left and right
    2. swap
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        order = []
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        ans = list(s)
        left, right = 0, len(ans)-1
        while left <= right:
            if ans[left] in vowels and ans[right] in vowels:
                ans[left], ans[right] = ans[right], ans[left]
                # Error 1: remember to change the pointer
                left += 1
                right -= 1
                # Error 2: continue to skip rest of conditions
                continue
            if ans[left] not in vowels:
                left += 1
            if ans[right] not in vowels:
                right -= 1
        return ''.join(ans)

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        order = []
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        ans = list(s)
        for i,char in enumerate(ans):
            if char in vowels:
                order.append(i)
        while len(order) > 1:
            left = order.pop(0)
            right = order.pop()
            ans[left], ans[right] = ans[right], ans[left]
        return ''.join(ans)

