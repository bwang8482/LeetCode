"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

"""Solution:
	1. sort the intervals and calculate the overlapping
	2. if the left side larger than previous left and smaller than previous right
	3. merge intervals
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
        	return []
        # Error1: using key = lambda x:x.start to sort the list by start
        intervals = sorted(intervals, key = lambda x:x.start)
        # Error2: assign first interval to left and right not inf and 0
        merged_intervals, left, right = [], intervals[0].start, intervals[0].end 
        for interval in intervals[1:]:
        	if interval.start <= right:
        		left = min(left, interval.start)
        		right = max(right, interval.end)
        	else:
        		merged_intervals.append([left,right])
        		left = interval.start
        		right = interval.end
        # Error3: push the last interval to list
        merged_intervals.append(Interval(left,right))
        return merged_intervals
