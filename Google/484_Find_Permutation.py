"""
By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4], which are both illegal constructing special string that can't represent the "DI" secret signature.

On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.

Example 1:
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where the number 1 and 2 construct an increasing relationship.
Example 2:
Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]
Note:

The input string will only contain the character 'D' and 'I'.
The length of input string is a positive integer and will not exceed 10,000
"""


"""Solution:
    1. this problem can be solved by two pointers.
    2. using one pointers to track the location of begining D.
    3. if new mark is D, insert the number before the first pointer
    4. if new mark is I, reallocate the first pointer to cuurent location and insert new number after pointer
"""


class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        left, right = [0], [1]
        for i,mark in enumerate(s):
            if mark == 'D':
                right = [i+2] + right
            else:
                left.extend(right)
                right = [i+2]
        left.extend(right)
        return left[1:]

"""Summary:
    this solution needs too much list manipulation. The algorithm is slow.
"""


"""Solution:
    1. this solution is more like a math solution.
    2. using one parameter to remember the begining of D.
    3. when meet 'I', print the string in descending order
"""
class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans = [0]
        prev = 0
        for i,mark in enumerate(s):
            if mark == 'I':
                ans.extend([x for x in range(i+1, prev, -1)])
                prev = i+1
        # remember to push the last substring.
        ans.extend([x for x in range(len(s)+1, prev, -1)])
        return ans[1:]

"""Summary:
    Remember the last part when using two pointers algorithm.
"""









