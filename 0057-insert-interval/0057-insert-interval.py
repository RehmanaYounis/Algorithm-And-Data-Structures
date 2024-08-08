class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        nstart,nend=newInterval
        for i in range(len(intervals)):
            start,end=intervals[i][0],intervals[i][1]
            if nend<start:
                res.append([nstart, nend])
                res+=intervals[i:]
                return res
            elif end<nstart:
                res.append(intervals[i])
            else:
                nstart=min(nstart, start)
                nend=max(nend, end)
        res.append([nstart,nend])
        return res
            