"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""

"""Solution
To find in linear time a longest palindrome in a string, an algorithm may take advantage of the following characteristics or observations about a palindrome and a sub-palindrome:

The left side of a palindrome is a mirror image of its right side.
(Case 1) A third palindrome whose center is within the right side of a first palindrome will have exactly the same length as that of a second palindrome anchored at the mirror center on the left side, if the second palindrome is within the bounds of the first palindrome by at least one character.
(Case 2) If the second palindrome meets or extends beyond the left bound of the first palindrome, then the third palindrome is guaranteed to have at least the length from its own center to the right outermost character of the first palindrome. This length is the same from the center of the second palindrome to the left outermost character of the first palindrome.
To find the length of the third palindrome under Case 2, the next character after the right outermost character of the first palindrome would then be compared with its mirror character about the center of the third palindrome, until there is no match or no more characters to compare.
(Case 3) Neither the first nor second palindrome provides information to help determine the palindromic length of a fourth palindrome whose center is outside the right side of the first palindrome.
It is therefore desirable to have a palindrome as a reference (i.e., the role of the first palindrome) that possesses characters furtherest to the right in a string when determining from left to right the palindromic length of a substring in the string (and consequently, the third palindrome in Case 2 and the fourth palindrome in Case 3 could replace the first palindrome to become the new reference).
Regarding the time complexity of palindromic length determination for each character in a string: there is no character comparison for Case 1, while for Cases 2 and 3 only the characters in the string beyond the right outermost character of the reference palindrome are candidates for comparison (and consequently Case 3 always results in a new reference palindrome while Case 2 does so only if the third palindrome is actually longer than its guaranteed minimum length).
For even-length palindromes, the center is at the boundary of the two characters in the middle.
"""


"""
Version 1: DP with O(N^2) runtime and O(N^2) space
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        dp = [[False for x in range(size)] for y in range(size)]
        longest = 1
        begin = 0
        # set all strings with length 1 to be True
        for i in range(size):
            dp[i][i] = True
        # set all same length 2 strings to be True
        for i in range(size-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                longest = 2
                begin = i
        # traverse for length and start point
        for length in range(3, size+1):
            for i in range(size-length+1):
                j = i + length - 1
                if (s[i] == s[j]) and (dp[i+1][j-1]):
                    dp[i][j] = True
                    longest = length
                    begin = i
        return s[begin:begin+longest]



"""
Version 2: DP with O(N^2) runtime and O(1) space, Center
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, left_center, right_center):
            l, r = left_center, right_center
            size = len(s)
            while l >= 0 and r < size and s[l] == s[r]:
                l -= 1
                r += 1
            return l, r-l+1

        size = len(s)
        longest = 1
        begin = 0
        if size == 0:
            return ""
        for i in range(size-1):
            begin_odd, len_odd = expand(s, i, i)
            begin_even, len_even = expand(s, i, i+1)
            if len_odd > longest:
                begin = begin_odd
                longest = len_odd
            if len_even > longest:
                begin = begin_even
                longest = len_even
        return s[begin:longest]



















