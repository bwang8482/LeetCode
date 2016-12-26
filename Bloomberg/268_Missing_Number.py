"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

"""Solution:
	1. calculate the sum and supposed sum
=>	2. Using bit manipulate: xor
		1) a^b^b = a
		2) 0^index^value should be 0
		3) if number missing, result will be the number.
"""
"""Error:
	1. It may overflow when calculating sum -> using average instead.
	2. floating issue when using average 
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # # average of 0...n, (0+n)*(n+1) / 2*(n+1) = n/2
        # origin = n/2.0
        # total = 0
        # for i in range(n):
        # 	# average of nums, total number is n
        # 	total += float(nums[i])/(n+1)
        # ret = (origin - total)*(n+1)
        # return int(ret)
        xor = len(nums)
        for i in range(len(nums)):
        	xor = xor ^ i ^ nums[i]
        return xor

