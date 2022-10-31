class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i>= len(text1) or j>= len(text2):
                return 0
            
            if text1[i]==text2[j]:
                dp[(i,j)]=1+ dfs(i+1, j+1)
                return dp[(i,j)]
            else:
                case1 =  dfs(i+1, j)
                case2 = dfs(i,j+1) #if j+1<len(text2) else 0
                dp[(i,j)]= max(case1, case2)
                return dp[(i,j)]

        return dfs(0,0)