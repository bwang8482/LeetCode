"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""


"""Solution:
    1. traverse every num in nums 32 times for 32 bits
    2. from MSB to LSB to determine the max value
"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            candidates = set()
            for num in nums:
                candidates.add(num & mask)
            target = ans | (1 << i)
            for candidate in candidates:
                # Tip: a^b=c --> b^c=a --> c^a=b
                if candidate ^ target in candidates:
                    ans = target
                    break
        return ans

"""Summary:
    the key idea is a^b=c --> b^c=a --> c^a=b. traverse the list 32 times for 32 bits.
"""










