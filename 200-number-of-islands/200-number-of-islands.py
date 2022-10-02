class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        visit=set()
        if not rows and not cols:
            return count
        def dfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=='0' or (r,c) in visit:
                return 
            visit.add((r,c))
            for cr,  cc in directions:
                nr = cr+r
                nc = cc+c
                dfs(nr, nc)
            
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visit and grid[row][col]=='1':
                    count+=1
                    dfs(row, col)
                    
        
        return count
            