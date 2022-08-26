class Solution(object):
    def findItinerary(self, tickets):
        tickets.sort()
        ticketMap=collections.defaultdict(list)
        for f,t in tickets:
            ticketMap[f].append(t)
        # print(ticketMap)
        visit=set()
        cycle=set()
        res=['JFK']
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True            
            for index,nei in enumerate(ticketMap[src]):
                res.append(nei)

                ticketMap[src].remove(nei)
                if dfs(nei): return True
                res.pop()
                ticketMap[src].insert(index,nei)
                
                
        dfs('JFK')
        return res