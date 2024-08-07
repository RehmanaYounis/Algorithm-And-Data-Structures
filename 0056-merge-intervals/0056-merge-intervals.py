class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        res=[intervals[0]]
        for start, end in intervals:
            cur_start=res[-1][0]
            cur_end=res[-1][1]
            
            if cur_end<start:
                res.append([start, end])
            else:
                res[-1][0]=min(start,cur_start)
                res[-1][1]=max(end, cur_end)
            
        return res
        