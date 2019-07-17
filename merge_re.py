'''
Quest:
    Given a collection of intervals, merge all overlapping intervals.

    Example 1:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Example 2:
    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

    NOTE: input types have been changed on April 15, 2019.
    Please reset to default code definition to get new method signature.

Solution:
    - use sorted(iterable, key, reverse)
'''


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):

        if not intervals:
            return []

        def startval(nums):
            return nums[0]

        res = []
        for i in sorted(intervals, key=startval):
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)

        return res

test = Solution()
intervals = [[1, 4], [4, 5]]
print(test.merge(intervals))