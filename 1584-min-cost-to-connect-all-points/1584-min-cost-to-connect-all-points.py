class Solution(object):
    def minCostConnectPoints(self, points):
        pointMap=collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1=points[i]
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                pointMap[i].append([dist, j])
                pointMap[j].append([dist, i])

        minHeap=[[0,0]]
        res=set()
        cost=0
        while len(res) < len(points):
            dist, point = heapq.heappop(minHeap)
            if point in res:
                    continue
            cost+=dist
            res.add(point)
            for d, nei in pointMap[point]:
                
                heapq.heappush(minHeap, [d , nei])
        return cost