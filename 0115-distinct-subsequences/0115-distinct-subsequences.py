class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp={}
        def dfs(i1, i2):
            if (i1,i2) in dp:
                return dp[(i1,i2)]
            if i2>=len(t):
                return 1
            if i1>=len(s):
                return 0
            
            
            
            
            if s[i1]==t[i2]:
                res= dfs(i1+1, i2+1)+dfs(i1+1, i2)
            else:
                res=dfs(i1+1, i2)
            dp[(i1,i2)]=res
            return dp[(i1,i2)]
        return dfs(0,0)