class Solution(object):
    def merge(self, intervals):
        stack=[]
        intervals=sorted(intervals)
        stack.append(intervals[0])
        prevStart, prevEnd=intervals[0]
        for i in range(1, len(intervals)):
            curStart,curEnd=intervals[i]
            if curStart <= prevEnd:
                stack[-1][0]=min(stack[-1][0], curStart)
                stack[-1][1]=max(stack[-1][1], curEnd)
            else:
                stack.append(intervals[i])
            prevStart,prevEnd=stack[-1]
        return stack
        