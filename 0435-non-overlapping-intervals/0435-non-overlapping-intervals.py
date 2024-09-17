class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevE=intervals[0][1]
        count=0
        for i in range(1, len(intervals)):
            curS,curE=intervals[i]
            if prevE>curS:
                count+=1
                prevE=min(prevE,curE)
            else:
                prevE=curE
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         intervals.sort()
#         prevEnd=intervals[0][1]
#         res=0
#         for start, end in intervals[1:]:
#             if start < prevEnd:
#                 res+=1
#                 prevEnd=min(end, prevEnd)
#             else:
#                 prevEnd=end
#         return res
                