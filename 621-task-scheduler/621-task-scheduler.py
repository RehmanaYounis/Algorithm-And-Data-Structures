class Solution(object):
    def leastInterval(self, tasks, n):
        time =0
        q=deque()
        TaskCounter=Counter(tasks)
        maxHeap = [-s for s in TaskCounter.values() ]
        heapq.heapify(maxHeap)
        
        while maxHeap or q:
            time+=1
            if not maxHeap:
                time = q[0][1]
            else:
                val = 1+heapq.heappop(maxHeap)
                if val != 0:
                    q.append([val, time+n])
            if q and q[0][1]==time:
                cur, _ = q.popleft()
                heapq.heappush(maxHeap, cur)
        return time
       

# count = Counter(tasks)
#         maxHeap = [-cnt for cnt in count.values()]
#         heapq.heapify(maxHeap)

#         time = 0
#         q = deque()  # pairs of [-cnt, idleTime]
#         while maxHeap or q:
#             time += 1

#             if not maxHeap:
#                 time = q[0][1]
#             else:
#                 cnt = 1 + heapq.heappop(maxHeap)
#                 if cnt:
#                     q.append([cnt, time + n])
#             if q and q[0][1] == time:
#                 heapq.heappush(maxHeap, q.popleft()[0])
#         return time




















