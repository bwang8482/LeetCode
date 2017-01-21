"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

"""Solution:
    1. this problem can be solved by two pointers
    2. one pointer for start time and the other for end time
    3. sort the start and end time separately and tarverse both list
    4. for each start time that ealier than end time, add one more room
    5. for each end time ealier than start time, empty one room
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts, ends, size = [], [], 0
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
            size += 1
        # Tip: sort start and end separately
        starts = sorted(starts)
        ends = sorted(ends)
        i, j, room, empty = 0, 0, 0, 0
        while i < size:
            if starts[i] < ends[j]:
                if empty == 0:
                    room += 1
                else:
                    empty -= 1
                i += 1
            else:
                empty += 1
                j += 1
        return room



















