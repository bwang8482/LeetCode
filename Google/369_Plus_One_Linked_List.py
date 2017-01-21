"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
"""

"""Solution:
    1. this problem can be solved by two pointer
    2. one pointer to traverse the linked list
    3. the other one point to the node that should add one.
    4. after adding one, traverse the second pointer and set all node behind to 0
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        i, j = dummy, dummy
        while i.next is not None:
            # Error 2: check the val of current i curosr
            if i.val != 9:
                j = i
            # Error 1: remember to move cursor
            i = i.next
        if i.val != 9:
            i.val += 1
        else:
            j.val += 1
            j = j.next
            # Error 3: check if current j curosr is none
            while j is not None:
                j.val = 0
                j = j.next
        return dummy if dummy.val else head



