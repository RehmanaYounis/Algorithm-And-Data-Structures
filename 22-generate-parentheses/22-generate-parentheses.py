class Solution(object):
    def generateParenthesis(self, n):
        stack=[]
        res = []
        
        def backTrack(openC, closeC):
            if openC==closeC==n:
                res.append(''.join(stack))
                return
            if openC< n:
                stack.append('(')
                backTrack(openC+1,closeC)
                stack.pop()
            if closeC<openC:
                stack.append(')')
                backTrack(openC,closeC+1)
                stack.pop()
        backTrack(0,0)
        return res
    
    
    