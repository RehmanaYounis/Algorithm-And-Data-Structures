class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        par=[i for i in range(len (isConnected))]
        rank=[1] * len(isConnected)
        edges=set()
        rows=len(isConnected)
        cols=len(isConnected[0])
        
        provinces=len(isConnected)
        print(provinces)
        def find(n):
            p = par[n]
            while p!=par[p]:
                p=par[p]
            return p
        
        def Union(n1,n2):
            p1=find(n1)
            p2=find(n2)
            if p1 ==p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True
        
#         for e1,e2 in edges:
#             if Union(e1, e2):
#                 provinces-=1
                
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c]==1:
                    if Union(r, c):
                        provinces-=1
        return provinces