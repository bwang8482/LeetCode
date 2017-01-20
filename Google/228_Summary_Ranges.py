"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

"""Solution:
    1. this problem can be solved by two pointers
    2. append the previous range if the current num exceed the previous range
    3. remember to push the last range at last
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        ans = []
        left, right = nums[0], nums[0]
        for num in nums:
            if num > right + 1:
                # Error 1: remember type, str()
                ans.append(str(left) + '->' + str(right) if left != right else str(left))
                left = num
            right = num
        # Error 2: remember push the last interval
        ans.append(str(left) + '->' + str(right) if left != right else str(left))
        return ans
