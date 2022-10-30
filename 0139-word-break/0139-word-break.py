class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={}
        def dfs(i):
            if i in dp: 
                return dp[i]
            if i>=len(s):
                return True
            for j in range(i, len(s)):
                word=s[i:j+1]
                if word in wordDict:
                    if dfs(j+1):
                        dp[i]=True
                        return dp[i]
            dp[i]=False
            return dp[i]
        return dfs(0)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dp={}
#         def dfs(i):
#             if i in dp:
#                 return dp[i]
#             if i>=len(s):
#                 return True
#             res=False
#             print(i)
#             for j in range(i, len(s)):
#                 word=s[i:j+1]
#                 if word in wordDict:
#                     res=dfs(j+1)
#                     if res:
#                         break
#             dp[i]=res
#             return dp[i]
#         return dfs(0)
                    