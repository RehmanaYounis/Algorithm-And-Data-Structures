class Solution(object):
    def lastStoneWeight(self, stones):
        stones=[-s for s in stones]
        
        heapq.heapify(stones)
        while len(stones)>1:
            x=-heapq.heappop(stones)
            y=-heapq.heappop(stones)
            res= abs(x-y)
            if res!=0:
                heapq.heappush(stones, -res)
        if len(stones)==1:
            return -stones[0]
        else:return 0