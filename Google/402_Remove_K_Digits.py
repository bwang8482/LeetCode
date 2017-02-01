"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


"""Solution 1: backtracking
    1. remove 1 digit from current num and push it to stack
    2. ==> it will exceed memory limitation
"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        self.size = len(num) - k
        if self.size <= 0:
            return '0'
        self.stack = [num]
        self.smallest = float('inf')
        self.visited = set()
        while self.stack:
            cur = self.stack.pop()
            length = len(cur)
            if length > self.size:
                for i in range(length):
                    string = cur[:i] +cur[i+1:]
                    if string not in self.visited:
                        self.stack.append(string)
                        self.visited.add(string)
            elif length <= self.size:
                self.smallest = min(int(cur), self.smallest)
        return str(self.smallest)

"""Solution:
    1. traverse from left to right and remove the digit that larger than its next digit
    2. remove the tariling digits that beyond the expected length
    3. remove leading zeroes
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        length = len(num) - k
        if length <= 0:
            return '0'
        stack = []
        for i,digit in enumerate(num):
            # pop digit that is larger than its right neighbor
            while len(stack) > 0 and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # convert list to string
        ans = ''.join([str(x) for x in stack])
        # remove leading zeros and trailing digits
        return str(int(ans[:length]))
        

"""Summary:
    This solution is more like a math solution. Removing the peak digits that will make the number smaller.
"""

