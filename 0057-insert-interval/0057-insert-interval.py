class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        nstart,nend=newInterval
        print(nstart,nend)
        for i in range(len(intervals)):
            start= intervals[i][0]
            end=intervals[i][1]
            if nend <start:
                res.append([nstart,nend])
                res+=intervals[i:]
                return res
            elif end < nstart:
                res.append([start,end])
            else:
                nstart=min(nstart,start)
                nend= max(nend,end)
        res.append([nstart,nend])
        return res
                
            