class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i>=len(s):
                return True
            res=False
            print(i)
            for j in range(i, len(s)+1):
                word=s[i:j+1]
                if word in wordDict:
                    res=dfs(j+1)
                    if res:
                        break
            dp[i]=res
            return dp[i]
        return dfs(0)
                    