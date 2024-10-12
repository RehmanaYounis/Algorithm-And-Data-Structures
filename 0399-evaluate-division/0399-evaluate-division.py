class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eMap=defaultdict(list)
        for ind,lst in enumerate(equations):
            a,b=lst
            eMap[a].append([b, values[ind]])
            eMap[b].append([a,1/values[ind]])
        print(eMap)
        
        def bfs(src,dest):
            if src not in eMap or dest not in eMap:
                return -1
            q=deque()
            q.append([src,1])
            visit=set()
            while q:
                node,weight=q.pop()
                if node==dest:
                    return weight
                for nei in eMap[node]:
                    curNode,curWeight=nei
                    if curNode not in visit:
                        visit.add(curNode)
                        q.append([curNode, weight*curWeight])
            return -1
        res=[]
        for elem in queries:
            res.append(bfs(elem[0],elem[1]))
        return res