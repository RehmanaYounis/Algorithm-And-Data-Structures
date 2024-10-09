class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows,cols=m,n
        dp={}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==rows-1 and j == cols-1:
                return 1
            if (i<0 or i>=rows) or (j<0 or j>=cols):
                return 0
            res= dfs(i+1,j) + dfs(i, j+1)
            dp[(i,j)]=res
            return res
        return dfs(0,0)