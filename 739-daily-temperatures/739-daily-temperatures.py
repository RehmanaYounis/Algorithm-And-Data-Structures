class Solution(object):
    def dailyTemperatures(self, temperatures):
        t=temperatures
        res=[0]*len(temperatures)
        stack=[]
        for i in range(len(t))[::-1]:
            while stack and stack[-1][1] <=t[i]:
                stack.pop()
            if stack and t[i]< stack[-1][1]:
                res[i]=stack[-1][0] - i
            stack.append([i, t[i]])
        return res
                
            