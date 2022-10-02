class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        stack=[]
        def dfs(j):
            if j>=len(s):
                res.append(stack[::])
            for i in range(j, len(s)):
                if self.isPal(s,j,i):
                    stack.append(s[j:i+1])
                    dfs(i+1)
                    stack.pop()
        dfs(0)
        return res
    
    def isPal(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True