class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        res = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            if res[-1][1] >= sorted_intervals[i][0]:
                res[-1][1] = (max(res[-1][1], sorted_intervals[i][1]))
            else:
                res.append(sorted_intervals[i])
                
        return res