"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

"""
Solution
1. DP solution to track the maximum when traverse from left to right
2. for each position, choose the maximum sum from A[i] and previous_sum + A[i]
3. choose the maximum subarray sum from all sums
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return
        max_sum = nums[0]
        subarray_sum = nums[0]
        for i in range(1, len(nums)):
        	subarray_sum = max(subarray_sum+nums[i], nums[i])
        	max_sum = max(max_sum, subarray_sum)
        return max_sum
