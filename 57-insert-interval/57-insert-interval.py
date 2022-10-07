class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        
        newStart=newInterval[0]
        newEnd=newInterval[1]
        for i in range(len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            
            if newEnd<start:
                res.append([newStart, newEnd])
                return res+ intervals[i:]
                
            if end<newStart:
                res.append([start, end])
            else:
                newStart=min(newStart, start)
                newEnd=max(newEnd, end)
        res.append([newStart, newEnd])
        return res