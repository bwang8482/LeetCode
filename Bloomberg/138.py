"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

"""
The random pointer points to any other node and it is important to check the duplicate of nodes.
The difficulites of this problem is that we cannot identify if the node exists or not.
Therefore, we need to find a method to record the node while traversing.
"""

"""
Solution:
1. copy the linked list
2. create hash table
3. assign random pointer according to hash table
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # corner case check
        if head is None:
            return None

        # first loop: copy the linked list
        head_cur = head	
        new_head = RandomListNode(head.label)
        new_cur = new_head
        # check next
        while head_cur.next is not None:
            new_cur.next = RandomListNode(head_cur.next.label)
            new_cur = new_cur.next
            head_cur = head_cur.next

        # second loop: create hash table
        address_map = {}
        head_cur = head
        new_cur = new_head
        while head_cur is not None:
            address_map[head_cur] = new_cur
            head_cur = head_cur.next
            new_cur = new_cur.next

        # third loop: assign random pointer
        head_cur = head
        new_cur = new_head
        while head_cur is not None:
            if head_cur.random is None:
                new_cur.random = None
            else:
                new_cur.random = address_map[head_cur.random]
            head_cur = head_cur.next
            new_cur = new_cur.next
        return new_head





