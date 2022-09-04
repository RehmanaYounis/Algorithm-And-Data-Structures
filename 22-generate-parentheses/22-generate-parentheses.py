class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def dfs(openB, closeB):
            if openB==closeB == n:
                res.append(''.join(stack))
                return
            if openB <n:          
                stack.append('(')
                dfs(openB+1, closeB)
                stack.pop()
            if closeB<openB:
                stack.append(')')
                dfs(openB, closeB+1)
                stack.pop()
        dfs(0,0)
        return res
                