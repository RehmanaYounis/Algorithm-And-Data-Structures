class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS =len(image)
        COLS=len(image[0])
        dire=[[1,0], [-1,0], [0,1],[0,-1]]
        visit=set()
        curCol=image[sr][sc]
        def dfs(r,c):
            if r<0 or r>=ROWS or c< 0 or c>=COLS or (r,c) in visit or image[r][c]!= curCol:
                return
            image[r][c]=color
            visit.add((r,c))
            for dr, dc in dire:
                nr=r+dr
                nc=c+dc
                dfs(nr,nc)
        dfs(sr,sc)
        return image
                
                
            