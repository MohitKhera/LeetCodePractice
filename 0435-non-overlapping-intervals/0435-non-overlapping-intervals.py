class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda i: i[1])
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] > intervals[i][0]:
                res += 1
                continue
            curr = intervals[i]

        return res