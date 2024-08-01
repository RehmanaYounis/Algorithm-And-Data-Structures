class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        
        stack=[]
        stack.append(intervals[0])
        for i in range(1, len(intervals)):
            if stack[-1][1] >= intervals[i][0]:
                stack[-1][1]=max(stack[-1][1], intervals[i][1])   
            else:
                stack.append(intervals[i])
        return stack       
    

#         for start, end in intervals:
#             lastEnd = output[-1][1]

#             if start <= lastEnd:
#                 # merge
#                 output[-1][1] = max(lastEnd, end)
#             else:
#                 output.append([start, end])
#         return output

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack=[]
#         intervals.sort(key= lambda i:i[0])
#         stack.append(intervals[0])
#         for i in range(1, len(intervals)):
#             start=intervals[i][0]
#             end=intervals[i][1]
#             if start <= stack[-1][1]:
#                 newStart, newEnd=stack.pop()
#                 newStart=min(newStart, start)
#                 newEnd=max(newEnd, end)
#                 stack.append([newStart, newEnd])
#             else:
#                 stack.append([start,end])
            
#         return stack        