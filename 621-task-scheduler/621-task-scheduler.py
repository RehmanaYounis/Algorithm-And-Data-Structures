class Solution(object):
    def leastInterval(self, tasks, n):
        taskCountMap=Counter(tasks)
        q=deque()
        time=0
        minHeap=[-s for s in taskCountMap.values()]
        heapq.heapify(minHeap)
        while minHeap or q:
            # print(minHeap, q)
            time+=1
            if minHeap:
                cur = 1+heapq.heappop(minHeap)
                if cur !=0:
                    q.append([cur,time+n])
            if q and q[0][1]==time:
                heapq.heappush(minHeap, q.popleft()[0])
        return time
            
        
       

