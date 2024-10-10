class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        total=0
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=='0' or grid[r][c]=='*':
                return 0
            grid[r][c]='*'
            print(r,c)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return 1
        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res+=dfs(r,c)
        return res