class Solution(object):
    def orangesRotting(self, grid):
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    grid[i][j]='*'
                    q.append([i, j])
                elif grid[i][j]==1:
                    fresh+=1
        if fresh ==0:
            return 0
        count=0
        time =0
        while q:
            for i in range(len(q)):
                x,y=q.popleft()
                
                for d in directions:
                    x1=x+d[0]
                    y1=y+d[1]
                    if x1>=0 and y1>=0 and x1<rows and y1<cols and grid[x1][y1]==1:
                        q.append([x1,y1])
                        # print(x1,y1)
                        grid[x1][y1]='*'
                        count+=1
            time+=1
            if count == fresh:
                return time
        return -1
          
                    
                    
       