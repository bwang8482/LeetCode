"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""

"""Solution:
    1. create dictionary
    2. using stack to match
"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        diction = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        left, right = 0, len(num)-1
        while left <= right:
            # Error 1: remember to check if key exist
            key = num[left]
            if key not in diction or diction[key] != num[right]:
                return False
            left += 1
            right -= 1
        return True
