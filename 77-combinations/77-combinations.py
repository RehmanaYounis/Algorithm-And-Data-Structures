class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        stack=[]
        def dfs(j):
            if len(stack) == k:
                res.append(stack[::])
            for i in range(j, n+1):
                stack.append(i)
                dfs(i+1)
                stack.pop()
        dfs(1)
        return res