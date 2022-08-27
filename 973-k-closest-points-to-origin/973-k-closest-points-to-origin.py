import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x,y in points:
            res= math.sqrt((x**2) + (y**2))
            heapq.heappush(minHeap, [res, [x,y]])
        result=[]
        print(minHeap)
        while k>0:
            v,crd= heapq.heappop(minHeap)
            result.append(crd)
            k-=1
        return result
        