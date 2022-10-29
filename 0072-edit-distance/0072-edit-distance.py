class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1=len(word1)
        len2=len(word2)
        if len1==0:
            return len2
        if len2==0:
            return len1
        if word1==word2:
            return 0
        dp={}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i>=len1 and j>=len2:
                return 0
            if i>=len1:
                return len2-j
            if j>=len2:
                return len1-i
            if word1[i]==word2[j]:
                res= dfs(i+1, j+1)
            else:
                res= min(1+dfs(i,j+1), 1+dfs(i+1, j), 1+dfs(i+1,j+1))
            dp[(i,j)]=res
            return dp[(i,j)]
        return dfs(0,0)