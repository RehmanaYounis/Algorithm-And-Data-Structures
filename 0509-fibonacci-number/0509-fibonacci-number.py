class Solution:
    def fib(self, n: int) -> int:
        dp={}
        def dfs(n):
            if n in dp:
                return dp[n]
            if n==0:
                return 0
            if n==1:
                return 1
            dp[n]=dfs(n-1)+dfs(n-2)
            return dp[n]
        return dfs(n)