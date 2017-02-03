"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


"""Solution:
    1. using two dp list, one for max, one for min.
    2. if new number is negative, multiply with min array
    3. if new number is positive, multiply with max array
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Error 1: product should be -inf, not 0
        product = -float('inf')
        length = len(nums)
        # dp list has length len(nums)+1, 0 means nothing.  
        maximum = [-float('inf') for i in range(length+1)]
        minimum = [float('inf') for i in range(length+1)]
        for i in range(length):
            if nums[i] < 0:
                maximum[i+1] = max(nums[i], nums[i] * minimum[i])
                minimum[i+1] = min(nums[i], nums[i] * maximum[i])
            else:
                maximum[i+1] = max(nums[i], nums[i] * maximum[i])
                minimum[i+1] = min(nums[i], nums[i] * minimum[i])
            product = max(product, maximum[i+1])
        return product


"""Summary:
    1. the key problem in dp is the index difference for nums and dp list.
    2. dp list should have one more element stands for initial state (0).
"""


"""Solution:
    1. we don't need 1d array for dp
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Error 1: product should be -inf, not 0
        product = -float('inf')
        length = len(nums)
        # actually we don't need 1d dp array.
        maximum, minimum = -float('inf'), float('inf')
        for i in range(length):
            if nums[i] < 0:
                # Error 2: modify maximum and minimum at the same time
                maximum, minimum = max(nums[i], nums[i] * minimum), min(nums[i], nums[i] * maximum)
            else:
                maximum, minimum = max(nums[i], nums[i] * maximum), min(nums[i], nums[i] * minimum)
            product = max(product, maximum)
        return product


"""Summary:
    there is no need to keep an 1d dp array.
"""






