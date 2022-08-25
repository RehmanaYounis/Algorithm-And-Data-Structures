class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pmap=collections.defaultdict(list)
        totalp=len(points)
        for p1 in range(totalp):
            for p2 in range(p1+1, totalp):
                dis = abs(points[p1][0]-points[p2][0]) + abs(points[p1][1]-points[p2][1])
                pmap[p1].append([dis,p2])
                pmap[p2].append([dis,p1])

        mHeap=[[0,0]]
        res=set()
        cost=0
        while len(res) < totalp:
            c, mpoint = heapq.heappop(mHeap)
            if mpoint in res:
                continue
            res.add(mpoint)
            cost+=c
            for val, nei in pmap[mpoint]:
                if nei not in res:
                    heapq.heappush(mHeap, [val, nei])
        return cost