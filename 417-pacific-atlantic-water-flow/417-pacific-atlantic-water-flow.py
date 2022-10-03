class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pac=set()
        atl=set()
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        def dfs(r,c, visit, curH):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or heights[r][c]<curH:
                return
            visit.add((r,c))
            curH=heights[r][c]
            for cr,cc in directions:
                nr=cr+r
                nc=cc+c
                dfs(nr,nc, visit,curH )
            
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
        
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
        
        for col in range(cols):
            dfs(rows-1, col, atl, heights[rows-1][col])
        
        for row in range(rows):
            dfs(row, cols-1, atl, heights[row][cols-1])
            
        res=[]
        for row in range(rows):
            for col in range(cols):
                if (row,col) in pac and (row,col) in atl:
                    res.append([row,col])
        return res
        
        