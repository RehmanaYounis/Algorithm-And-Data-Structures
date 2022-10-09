class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        stack=[]
        intervals.sort(key = lambda i:i[0])
        stack.append(intervals[0])
        count=0
        print(intervals)
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if start>=stack[-1][1]:
                stack.append([start,end])
            else:
                
                count+=1
                newStart, newEnd= stack.pop()
                newdist=abs(newStart- newEnd)
                
                if newEnd>end:
                    stack.append([start, end])
                else:
                    stack.append([newStart, newEnd])
        return count