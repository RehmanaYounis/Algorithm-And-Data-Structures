class Solution:
    def numDecodings(self, s: str) -> int:
        dp={}
        def dfs(i):
            if i == len(s):
                return 1
            if s[i]=='0':
                return 0
            if i in dp:
                return dp[i]
            ans = dfs(i+1)
            if (i+1< len(s) and (s[i]=='1' or s[i]=='2' and s[i+1] in ('01234560'))):
                ans+=dfs(i+2)
            dp[i]=ans
            return ans
        return dfs(0)