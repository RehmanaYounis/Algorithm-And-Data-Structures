class Solution(object):
    def insert(self, intervals, newInterval):
        newStart= newInterval[0]
        newEnd= newInterval[1]
        res=[]
        for i, (curStart, curEnd) in enumerate(intervals):
            if newEnd<curStart:
                res.append([newStart,newEnd])
                res+=intervals[i:]
                return res
            elif curEnd < newStart:
                res.append([curStart, curEnd])
            else:
                newStart= min(newStart, curStart)
                newEnd = max(newEnd, curEnd)
        res.append([newStart, newEnd])
        return res
            
                
        