class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        total=0
        q=deque()
        directions=[[1,0], [-1, 0], [0,1], [0,-1]]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    q.append([row,col])
                elif grid[row][col]==1:
                    total+=1
        
        time=0
        while q and total>0:
            for _ in range(len(q)):
                cr,cc=q.popleft()
                
                for row,col in directions:
                    nr=cr+row
                    nc=cc+col
                    
                    if (nr in range(rows) and nc in range(cols) 
                        and grid[nr][nc] == 1):
                        q.append([nr,nc])
                        grid[nr][nc]=2
                        total-=1
            time+=1
        if total == 0: return time
        else: return -1
                        
                    
                    
                
                
                
                
                