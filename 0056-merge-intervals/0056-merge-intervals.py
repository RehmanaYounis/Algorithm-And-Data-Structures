class Solution(object):
    def merge(self, intervals):
        intervals=sorted(intervals)
        prev=intervals[0][1]
        stack=[intervals[0]]
        for i in range(1, len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            if prev >= start:
                stack[-1][0]=min(stack[-1][0],start)                
                stack[-1][1]=max(prev,end)
            else:
                stack.append([start,end])
            prev=stack[-1][1]
        return stack

            
        