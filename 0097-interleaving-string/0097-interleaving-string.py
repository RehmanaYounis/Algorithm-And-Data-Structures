class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        dp={}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i>=len(s1) and j >=len(s2):
                return True
            case1=False
            case2=False
            if i<len(s1) and s1[i]==s3[i+j]:
                case1= dfs(i+1, j)
            if j<len(s2) and s2[j]==s3[i+j]:
                case2= dfs(i, j+1)
            dp[(i,j)]=case1 or case2
            
            return dp[(i,j)]
        return dfs(0,0)