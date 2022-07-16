class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        T=temperatures
        res=[0]*len(temperatures)
        for i in reversed(range(len(temperatures))):
            while stack and T[i]>=stack[-1][0]:
                stack.pop()
            if stack and T[i]<stack[-1][0]:
                res[i]=stack[-1][1] - i
            stack.append([T[i], i])
        return res