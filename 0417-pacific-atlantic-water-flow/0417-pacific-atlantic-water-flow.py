class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pacific=[]
        atlantic=[]
        grid=heights
        def dfs(r,c,preVal, stack):
            if r<0 or r>=rows or c<0 or c>=cols or heights[r][c]<preVal or [r,c] in stack:
                return
            stack.append([r,c])
            dfs(r+1,c,grid[r][c], stack)
            dfs(r-1,c,grid[r][c], stack)
            dfs(r,c+1,grid[r][c], stack)
            dfs(r,c-1,grid[r][c], stack)
        for col in range(cols):
            dfs(0,col,grid[0][col], pacific)
            dfs(rows-1,col,grid[rows-1][col], atlantic)
        for row in range(rows):
            dfs(row,0,grid[row][0], pacific)
            dfs(row,cols-1,grid[row][cols-1], atlantic)
        res=[]
        for  r in range(rows):
            for c in range(cols):
                if [r,c] in pacific and [r,c] in atlantic:
                    res.append([r,c])
        return res
        