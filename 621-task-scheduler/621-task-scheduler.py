class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tmap=Counter(tasks)
        q=deque()
        time=0
        minHeap=[-s for s in tmap.values()]
        heapq.heapify(minHeap)
        while q or minHeap:
            time+=1
            if minHeap:
                cur = 1 + heapq.heappop(minHeap)
                if cur:
                    q.append([cur, time+n])
            if q and q[0][1] ==time:
                heapq.heappush(minHeap,q.popleft()[0])
                
        return time
        

















