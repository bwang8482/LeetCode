"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
"""

"""Solution:
    1. Boyer-Moore method to count the majority number
    2. for each num, if it is candidate, increase the count
    3. if it not a candiate, decrease the counts for all candidate
    4. check the candidates
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_1, num_2, count_1, count_2 = 0, 1, 0, 0
        for num in nums:
            if num == num_1:
                count_1 += 1
            elif num == num_2:
                count_2 += 1
            elif count_1 == 0:
                num_1 = num
                count_1 = 1
            elif count_2 == 0:
                num_2 = num
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        return [x for x in num_1, num_2 if nums.count(x) > len(nums)/3.0]


