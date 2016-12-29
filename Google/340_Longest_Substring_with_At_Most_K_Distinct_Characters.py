"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""

"""Solution
1. use dictionary to track the rightmost location of each characters
2. if number larger than k, remove the character with smallest rightmost
"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Error 2 -> remember to check k = 0, otherwist remove_key will out of index
        if k == 0:
            return 0
        longest = 0
        diction = {}
        begin = 0
        number = 0
        for i in range(len(s)):
            if s[i] not in diction:
                if number == k:
                    remove_key = sorted(diction, key=diction.get)[0]
                    begin = diction[remove_key] + 1
                    diction.pop(remove_key, None)
                    number -= 1
                diction[s[i]] = i
                number += 1
                longest = max(longest, i-begin+1)
            else:
                diction[s[i]] = i
                # Error 1 -> longest += 1; the longest will be modified
                longest = max(longest, i-begin+1)
        return longest
