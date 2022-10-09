class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack=[]
        intervals.sort(key= lambda i:i[0])
        stack.append(intervals[0])
        for i in range(1, len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            if start <= stack[-1][1]:
                newStart, newEnd=stack.pop()
                newStart=min(newStart, start)
                newEnd=max(newEnd, end)
                stack.append([newStart, newEnd])
            else:
                stack.append([start,end])
            
        return stack        