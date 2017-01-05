"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

"""Solution:
    1. the order of each people will only be affected by people tailer than him
    2. sort the people by height first
    3. for group of people have same height, sort them by k
    4. place the people in queue
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []

        queue = []
        # Tip: sorted the array by lambda function. key in pair.
        # Error 1: -x[0] from large to small
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        for person in people:
            # Tip: using insert function
            # Error 2: first is index and second is element
            queue.insert(person[1], person)
        return queue


