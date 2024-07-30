class Solution(object):
    def numIslands(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        total=0
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or grid[r][c] == "0": return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] =="1":
                    total+=1
                    dfs(r,c)
        return total
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count=0
#         rows=len(grid)
#         cols=len(grid[0])
#         visit=set()
#         def dfs(r,c):
#             if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or grid[r][c]=='0':
#                 return
#             visit.add((r,c))
#             dfs(r+1,c)
#             dfs(r-1,c)
#             dfs(r,c+1)
#             dfs(r,c-1)
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col]=='1' and (row,col) not in visit:
#                     count+=1
#                     dfs(row,col)
#         return count
        