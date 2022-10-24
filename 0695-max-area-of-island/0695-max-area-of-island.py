class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        maxArea=0
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] !=1:
                return 0
            count=0
            grid[r][c]='*'
            d1=dfs(r+1,c)
            d2=dfs(r-1,c)
            d3=dfs(r,c+1)
            d4=dfs(r,c-1)
            return 1+(d1+d2+d3+d4)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxArea=max(maxArea,dfs(r,c))
        return maxArea