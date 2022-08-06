class Solution(object):
    def partition(self, s):
        res=[]
        stack=[]
        string=s
        def isPal(j):
            if j >= len(string):
                res.append(stack[::])
                return

            for i in range(j,len(string)):
                curStr=string[j:i+1]
                if curStr == curStr[::-1]:
                    stack.append(string[j:i+1])
                    isPal(i+1)
                    stack.pop()
        isPal(0)
        return res