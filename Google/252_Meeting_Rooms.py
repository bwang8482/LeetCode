"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""

"""Solution:
    1. sort the intervals and traverse from begin to end
    2. return false if left ealier than end
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals: return True
        # Error 1: remember to use lambda function to sort
        intervals = sorted(intervals, key=lambda interval:interval.start)
        right, left = 0, float('inf')
        for interval in intervals:
            left = interval.start
            if left < right:
                return False
            right = interval.end
        return True













