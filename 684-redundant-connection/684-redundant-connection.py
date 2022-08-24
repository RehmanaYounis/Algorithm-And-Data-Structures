class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par=[i for i in range( len(edges)+1)]
        rank = [1]*(len(edges)+1)
        
        def findParent(n):
            p=par[n]
            while p != par[p]:
                p=par[p]
            return p
        
        def Union(n1,n2):
            p1=findParent(n1)
            p2=findParent(n2)
            
            if p1 == p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True
        
        for e in edges:
            if not Union(e[0], e[1]):
                return [e[0],e[1]]
            