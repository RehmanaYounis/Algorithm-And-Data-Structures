class Solution(object):
    def leastInterval(self, tasks, n):
        time=0
        taskCount=Counter(tasks)
        q=deque()
        tasks=[-x for x in taskCount.values()]
        heapq.heapify(tasks)
        while tasks or q:
            time+=1
            # print(tasks, q)
            if tasks:
                cur = (heapq.heappop(tasks))
                cur+=1
                if cur:
                    q.append([cur, time+n])
            if q and q[0][1]==time:
                curLeft, curTime = q.popleft()
                heapq.heappush(tasks, curLeft)
        return time
            