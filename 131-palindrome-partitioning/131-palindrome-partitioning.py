class Solution(object):
    def partition(self, s):
        res=[]
        stack=[]
        def isPal(j):
            if j >= len(s):
                res.append(stack[::])
                return

            for i in range(j,len(s)):
                curStr=s[j:i+1]
                if curStr == curStr[::-1]:
                    stack.append(s[j:i+1])
                    isPal(i+1)
                    stack.pop()
        isPal(0)
        return res