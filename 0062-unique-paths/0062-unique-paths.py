class Solution(object):
    def uniquePaths(self, m, n):
        dp={}
        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            if r<0 or r>=m or c<0 or c>=n:
                return 0
            if (r == m-1 and c==n-1):
                return 1
            dp[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            return dp[(r,c)]
        return dfs(0,0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         total=m+n-2
#         r=m-1
#         res=1
#         for i in range(1,r+1):
#             res= res *(total-r+i)//i
#         return res