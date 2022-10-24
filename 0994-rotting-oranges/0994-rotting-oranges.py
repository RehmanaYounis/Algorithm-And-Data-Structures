class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                if grid[r][c]==1:
                    fresh+=1
        print(q)
        time=0
        visit=set()
        direc=[[1,0],[-1,0],[0,1],[0,-1]]
        while fresh>0 and q:
            for _ in range(len(q)):
                row,col=q.popleft()
                print(row,col)
                for cr,cc in direc:
                    r=row+cr
                    c=col+cc
                    if r<0 or r>=rows or c<0 or c>= cols or (r,c) in visit or grid[r][c]!=1:
                        continue
                    grid[r][c]=2
                    q.append([r,c])
                    visit.add((r,c))
                    fresh-=1
            time+=1
        return time if fresh==0 else -1
                