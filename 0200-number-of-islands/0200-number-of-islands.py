class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        count=0
        
        
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!='1':
                return
            grid[r][c]='*'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        
        for r in range(rows):
            for c in range(cols):
                # print(visit, r, c, (r,c)  in visit)
                # print(grid)
                if grid[r][c]=='1':
                    count+=1
                    dfs(r,c)
                    
        return count
                    