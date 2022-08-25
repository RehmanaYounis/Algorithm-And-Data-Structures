class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
       
        prices=[float('inf')] * n
        prices[src]=0
        res=0
        
        for i in range(k+1):
            temp=prices.copy()
            
            for i, nei, pr in flights:
                if prices[i]==float('inf'):
                    continue
                if pr+prices[i]<temp[nei]:
                    temp[nei]=pr+prices[i]
            prices=temp
        return prices[dst] if prices[dst]!= float('inf') else -1
    
    