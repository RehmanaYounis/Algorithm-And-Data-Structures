class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:                   # Check if the grid is empty
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or grid[r][c]=='*':
                return
            grid[r][c] = '*'  # Mark visited
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)   # Perform DFS to mark the entire island
                    res += 1    # Increment count for the island
        
        return res
