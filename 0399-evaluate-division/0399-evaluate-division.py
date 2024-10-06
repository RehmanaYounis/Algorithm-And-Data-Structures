class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eMap = defaultdict(list)
        for i, val  in enumerate(equations):
            a,b = val
            eMap[a].append([b,values[i]])
            eMap[b].append([a,1/values[i]])
        
        def bfs(src,target):
            if src not in eMap or target not in eMap: return -1
            q=deque()
            q.append([src,1])
            visited=set()
            visited.add(src)
            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for nei in eMap[node]:
                    nxt, val = nei
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append([nxt, val*w])
            return -1
        res=[]   
        for quer in queries:
            src,target=quer
            res.append(bfs(src,target))
        return res
        
