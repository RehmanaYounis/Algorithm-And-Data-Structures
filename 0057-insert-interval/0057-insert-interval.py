class Solution(object):
    def insert(self, intervals, newInterval):
        res=[]
        new_start, new_end=newInterval
        for i in range(len(intervals)):
            cur_start=intervals[i][0]
            cur_end=intervals[i][1]
            
            
            if new_end < cur_start:
                res.append([new_start,new_end])
                res+=intervals[i:]
                return res
            
            elif cur_end < new_start:
                res.append(intervals[i])
            
            else:
                new_start=min(new_start, cur_start)
                new_end=max(new_end,cur_end)
                
        res.append([new_start, new_end])
        return res
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
#         for i in range(len(intervals)):
#             if newInterval[1]<intervals[i][0]:
#                 res.append(newInterval)
#                 res+=intervals[i:]
#                 return res
#             elif newInterval[0]>intervals[i][1]:
#                 res.append(newInterval)
#             else:
#                 newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
#         res.append(newInterval)
#         return res
                
        