class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res+=intervals[i:]
                return res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res
      
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
        
#         newStart=newInterval[0]
#         newEnd=newInterval[1]
#         for i in range(len(intervals)):
#             start=intervals[i][0]
#             end=intervals[i][1]
            
#             if newEnd<start:
#                 res.append([newStart, newEnd])
#                 return res+ intervals[i:]
                
#             if end<newStart:
#                 res.append([start, end])
#             else:
#                 newStart=min(newStart, start)
#                 newEnd=max(newEnd, end)
#         res.append([newStart, newEnd])
#         return res