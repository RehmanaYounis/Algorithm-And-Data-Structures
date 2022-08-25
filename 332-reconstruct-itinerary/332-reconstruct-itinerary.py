class Solution(object):
    def findItinerary(self, tickets):
        tickets.sort()
        tmap=collections.defaultdict(list)
        for f, t in tickets:
            tmap[f].append(t)
        
        res=['JFK']
       
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in tmap:
                return False
            for i, nei in enumerate(tmap[src]):
                res.append(nei)
                tmap[src].remove(nei)
                if (dfs(nei)):return True
                res.pop()
                tmap[src].insert(i,nei)
        
        dfs('JFK')
        return res
                
                
                
        