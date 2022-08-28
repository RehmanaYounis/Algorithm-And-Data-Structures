class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskc=Counter(tasks)
        maxHeap= [-s for s in taskc.values()]
        heapq.heapify(maxHeap)
        q=deque()
        time=0
        while q or maxHeap:
            time+=1
            if maxHeap:
                curV = 1+heapq.heappop(maxHeap)
                if curV != 0:
                    q.append([curV, time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time















