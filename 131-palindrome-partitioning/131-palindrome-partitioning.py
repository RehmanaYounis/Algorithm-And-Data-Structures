class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        stack=[]
        def dfs(j):
            if j>=len(s):
                res.append(stack[::])
                return
            for i in range(j, len(s)):
                curWord = s[j:i+1]
                if curWord == curWord[::-1]:
                    stack.append(curWord)
                    dfs(i+1)
                    stack.pop()
        dfs(0)
        return res