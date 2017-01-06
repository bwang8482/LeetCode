"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
"""

"""Solution:
    1. calculate if the sum of all small rectangles equal to the sum of large rectangle
    2. there are only four corners
    3. each point cannot represent same type of corner more than once
    4. the type of each point must be even
"""

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        points = {}
        duplicate = set()
        area = 0
        left_x, left_y, right_x, right_y = float('inf'), float('inf'), 0, 0
        for rectangle in rectangles:
            # check for the area
            area += (rectangle[3]-rectangle[1])*(rectangle[2]-rectangle[0])
            left_x = min(left_x, rectangle[0])
            left_y = min(left_y, rectangle[1])
            right_x = max(right_x, rectangle[2])
            right_y = max(right_y, rectangle[3])
            # check for duplicate corners
            corners = [((rectangle[0], rectangle[3]), 0b0100),((rectangle[0], rectangle[1]), 0b1000),
                       ((rectangle[2], rectangle[3]), 0b0010),((rectangle[2], rectangle[1]), 0b0001)]
            for corner in corners:
                if corner[0] not in points:
                    points[corner[0]] = 0b0000
                if points[corner[0]] & corner[1]:
                    return False
                points[corner[0]] |= corner[1]
                # offset the corner types
                if corner[0] not in duplicate:
                    duplicate.add(corner[0])
                else:
                    duplicate.remove(corner[0])
        # if the corner number is not 4, return false
        if len(duplicate) != 4:
            return False
        return (area == (right_x - left_x)*(right_y - left_y))













