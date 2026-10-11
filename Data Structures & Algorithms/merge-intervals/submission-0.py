class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = []
        for interval in intervals:
            if len(res)>0:
                prev = res[-1]
                if interval[0] >= prev[0] and interval[0] <= prev[1]:
                    prev[0] = min(prev[0], interval[0])
                    prev[1] = max(prev[1], interval[1])
                else:
                    res.append(interval)
            else:
                res.append(interval)
        return res
