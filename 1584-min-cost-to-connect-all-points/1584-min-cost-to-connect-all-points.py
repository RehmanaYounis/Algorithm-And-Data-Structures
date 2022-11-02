class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pMap=defaultdict(list)
        N=len(points)
        for i in range(N):
            x1,y1=points[i]
            for j in range(i+1, N):
                x2,y2=points[j]
                dist =abs(x1-x2)+abs(y1-y2)
                pMap[i].append([dist, j])
                pMap[j].append([dist, i])
                
        
        heap=[[0,0]]
        res=0
        visit=set()
        while len(visit)< len(points):
            # print(heap, len(visit))
            cost, point=heapq.heappop(heap)
            if point in visit:
                continue
            
            visit.add(point)
            res+=cost

            for curCost, nei in pMap[point]:
                if nei not in visit:
                    heapq.heappush(heap, [curCost, nei])
        return res