"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.
"""

"""Solution: -> O(n^2)
    1. O(n^2) solution for this question is trivial
    2. we set two pointer i, j and j indicates the last bit of substring
    3. i indicates the bit before j.
    4. using dp to track the length
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        size = len(nums)
        dp = [1 for _ in range(size)]
        # for each element, traverse the element before and find the longest length
        for j in range(1,size):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)
        return sorted(dp)[-1]


"""Solution: -> O(nlogn)
    1. this question can be solved with O(nlogn) runtime if we use binary search.
    2. build a dp array to contain the smallest value for the string with different length
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        length = 0
        for i,num in enumerate(nums):
            if not dp or num > nums[dp[-1]]:
                dp.append(i)
                length += 1
            else:
                left, right = 0, len(dp)-1
                while left <= right:
                    mid = left + (right-left)/2
                    if nums[dp[mid]] == num:
                        left = mid
                        break
                    elif nums[dp[mid]] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                dp[left] = i
        return length












