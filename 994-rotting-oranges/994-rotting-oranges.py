class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        time=0
        # if grid[0][0]!=2:
            
        for r in range (rows):
            for c in range (cols):
                if grid[r][c]==2:
                    q.append([r,c])
                if grid[r][c]==1:
                    fresh+=1
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while fresh>0 and q:
            
            for _ in range(len(q)):
                r,c=q.popleft()
                for cr,cc in directions:
                
                    rm=r+cr
                    cm=c+cc

                    if (rm<0 or cm<0 or rm==rows or cm==cols or grid[rm][cm]!=1):
                        continue
                    grid[rm][cm]=2
                    q.append([rm,cm])
                    fresh-=1
            time+=1
       
        return time if fresh==0 else -1
        