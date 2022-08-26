class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        minHeap=[[grid[0][0],0,0]]
        t= grid[0][0]
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visit=set()
        visit.add((0,0))
        while minHeap:
            curT, r,c= heapq.heappop(minHeap)
            if r==n-1 and c == n-1:
                return curT
            for dr , dc in directions:
                nr, nc = r+dr , c+dc
                if (nr<0 or nc<0 or nr==n or nc==n or (nr,nc) in visit ):
                    continue
                heapq.heappush(minHeap, [max(curT,grid[nr][nc]), nr,nc])
                visit.add((nr,nc))
        