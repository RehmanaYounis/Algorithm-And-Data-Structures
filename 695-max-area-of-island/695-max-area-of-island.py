class Solution(object):
    def maxAreaOfIsland(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        maxArea=0
        def dfs(r,c):
            if r<0 or r>=rows or c <0 or c >= cols or (r,c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            return 1+ dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        
        for row in range(rows):
            for col in range(cols):
                maxArea=max(maxArea, dfs(row,col))
        
        return maxArea       
                