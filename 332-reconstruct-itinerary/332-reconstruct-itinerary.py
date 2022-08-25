class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        tmap=collections.defaultdict(list)
        for src,des in tickets:
            tmap[src].append(des)
        res=['JFK']
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in tmap:
                return False
            
            for index,nei in enumerate(tmap[src]):
                res.append(nei)
                tmap[src].pop(index)
                if dfs(nei): return True
                res.pop()
                tmap[src].insert(index,nei)
            return False
        dfs('JFK')
        return res