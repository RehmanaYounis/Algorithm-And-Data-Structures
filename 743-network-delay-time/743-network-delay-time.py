class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nmap=collections.defaultdict(list)
        for u,v,w in times:
            nmap[u].append([v,w])
        
        time=0
        minHeap=[[0,k]]
        visit=set()
        while minHeap:
            w,node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time=w
            for nei,cw in nmap[node]:
                if not nei in visit:
                    heapq.heappush(minHeap, [cw+w, nei])
        print(len(visit))
        return time if len(visit)==n else -1