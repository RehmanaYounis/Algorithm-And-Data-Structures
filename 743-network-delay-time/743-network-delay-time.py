class Solution(object):
    def networkDelayTime(self, times, n, k):
        nmap=collections.defaultdict(list)
        for u,v,w in times:
            nmap[u].append([v,w])
        
        visit=set()
        time=0
        minHeap=[[0,k]]
        while minHeap:
            w,src = heapq.heappop(minHeap)
            
            if src in visit:
                continue
            time=w
            visit.add(src)
            for des,dp in nmap[src]:
                if  not des in visit:
                    heapq.heappush(minHeap, [w+dp,des])
        return time if len(visit)==n else -1
    
 