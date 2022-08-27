class Solution(object):
    def networkDelayTime(self, times, n, k):
        nmap=collections.defaultdict(list)
        for u,v,w in times:
            nmap[u].append([v,w])
        minHeap=[[0,k]]
        visit=set()
        time =0
        while minHeap:
            curW, curN = heapq.heappop(minHeap)
            
            if curN in visit:
                continue
            visit.add(curN)
            time=curW
            for neig,ncost in nmap[curN]:
                if neig not in visit:
                    heapq.heappush(minHeap,[curW+ncost, neig])
                   
        return time if len(visit)==n else -1
            