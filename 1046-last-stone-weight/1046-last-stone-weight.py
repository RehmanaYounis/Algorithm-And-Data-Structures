class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)
        print(stones,minHeap)
        while len(minHeap)> 1:
            n1=abs(heapq.heappop(minHeap))
            n2=abs(heapq.heappop(minHeap))
            res = abs(n1-n2)
            if res>0:
                heapq.heappush(minHeap, -res)
    
        if len(minHeap) == 1:
            return -minHeap[0]
        else: return 0