class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res=[]
        res.append(intervals[0])
        
        for i in range(1,len(intervals)):
            prevS,prevE=res[-1][0], res[-1][1]
            curS,curE=intervals[i][0], intervals[i][1]
            if prevE<curS:
                res.append(intervals[i])
            else:
                res[-1][0], res[-1][1]=min(prevS,curS), max(prevE,curE)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         intervals.sort()
#         res=[]
#         curS,curE=intervals[0]
#         res.append([curS,curE])
#         for i in range(1,len(intervals)):
#             curS,curE=res[-1]
#             nextS,nextE=intervals[i]
#             if curE<nextS:
#                 res.append([nextS,nextE])
#                 curS=nextS
#                 curE=nextE
#             else:
#                 res[-1][0]=min(res[-1][0], nextS)
#                 res[-1][1]=max(res[-1][1],nextE)
            
#         return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
#         intervals.sort(key=lambda i:i[0])
#         res=[intervals[0]]
#         prev = intervals[0][1]
#         for i in range(1, len(intervals)):
#             cur_start=intervals[i][0]
#             cur_end=intervals[i][1]
            
#             if prev < cur_start:
#                 res.append([cur_start,cur_end])
#             else:
#                 res[-1][1]=max(cur_end,prev )
                
#             prev=max(prev, cur_end)
            
#         return res
            
                
                