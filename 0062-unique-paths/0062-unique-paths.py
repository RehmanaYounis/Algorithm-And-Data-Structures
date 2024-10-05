class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows,cols=m,n
        @cache
        def dfs(r,c):
            if r< 0 or r >=rows or c< 0 or c>=cols:
                return 0
            if r==(m-1) and c ==(n-1):
                return 1
            return dfs(r+1,c)+dfs(r,c+1)
        return dfs(0,0)
            
        
        
        
        
        
        
        
        
        
        
        
        
#         rows=m
#         cols=n
#         dp={}
#         def dfs(r,c):
#             if (r,c) in dp:
#                 return dp[(r,c)]
#             if r<0 or r>=m or c<0 or c>=n:
#                 return 0
#             if r==m-1 and c==n-1:
#                 return 1
#             R=dfs(r+1,c)
#             C=dfs(r, c+1)
#             dp[(r,c)]=R+C
#             return dp[(r,c)]
#         return dfs(0,0)
        