class Solution(object):
    def swimInWater(self, grid):
        minHeap=[[grid[0][0],0,0]]
        time=0
        end=len(grid)-1
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visit=set()
        visit.add((0,0))
        while minHeap:
            curTime, r,c=heapq.heappop(minHeap)
            if r==end and c==end:
                return curTime
            for dr,dc in directions:
                nr,nc=r+dr, c+dc
                if nr<0 or nc<0 or nr>end or nc>end or (nr,nc)in visit:
                    continue
                heapq.heappush(minHeap, ([max(curTime,grid[nr][nc]), nr,nc]))
                visit.add((nr,nc))

                
        
        