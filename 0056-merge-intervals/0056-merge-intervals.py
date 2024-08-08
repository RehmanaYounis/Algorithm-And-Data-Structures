class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        res=[intervals[0]]
        prevStart=intervals[0][0]
        prevEnd=intervals[0][1]
        
        for start, end in intervals:
            if prevEnd<start:
                res.append([start,end])
            else:
                res[-1][1]=max(prevEnd, end)
            prevEnd=max(prevEnd, end)
        return res
                
        