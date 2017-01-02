"""
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""

"""Solution:
    1. left to track small boundary
    2. right to track larger boundary
    3. for each boundary, compare with upper
"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        nums = sorted(nums)
        left = lower
        right = upper
        for num in nums:
            # Error 1: larger boundary should be num-1 <= upper
            if num - 1 <= upper:
                right = num - 1
            else:
                break
            if right == left:
                ans.append(str(left))
            elif right > left:
                ans.append(str(left) + '->' + str(right))
            left = num + 1
        # Error 2: remember to check the last boundary to upper
        if upper == left:
            ans.append(str(left))
        elif upper > left:
            ans.append(str(left) + '->' + str(upper))
        return ans
