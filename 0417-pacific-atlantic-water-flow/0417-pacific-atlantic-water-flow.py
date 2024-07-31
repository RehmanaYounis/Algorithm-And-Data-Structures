class Solution(object):
    def pacificAtlantic(self, heights):
        rows, cols=len(heights), len(heights[0])
        pac,atl=[],[]
        def dfs(r,c,visit,maxVal):
            if (r<0 or c<0 or r>=rows or c>=cols or [r,c] in visit or heights[r][c] < maxVal):
                return 
            visit.append([r,c])
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
            return
            
            
            
            
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        res=[]
        for r in range(rows):
            for c in range(cols):
                if [r,c] in pac and [r,c] in atl:
                    res.append([r,c])
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         pgrp=set()
#         agrp=set()
#         res=[]
#         rows=len(heights)
#         cols=len(heights[0])
        
#         def dfs(r,c,curVal,visited):
#             if (r<0 or c<0 or r==rows or c==cols or (r,c) in visited or heights[r][c]<curVal):
#                 return
#             visited.add((r,c))
#             dfs(r+1,c,heights[r][c], visited)
#             dfs(r-1,c,heights[r][c], visited)
#             dfs(r,c+1,heights[r][c], visited)
#             dfs(r,c-1,heights[r][c], visited)
          
         
#         for c in range (cols):
#             dfs(0,c,heights[0][c],pgrp)
#             dfs(rows-1,c,heights[rows-1][c],agrp)
            
#         for r in range (rows):
#             dfs(r,0, heights[r][0],pgrp)
#             dfs(r,cols-1,heights[r][cols-1],agrp )
        
      
#         for r in range (rows):
#             for c in range(cols):
#                 if (r,c) in pgrp and (r,c) in agrp:
#                     res.append([r,c])
        
#         return res
    
    