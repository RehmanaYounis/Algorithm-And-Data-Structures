class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(i,status):
            if (i,status) in dp:
                return dp[(i,status)]
            if i>=len(prices):
                return 0
            
            if status=='buy':
                case1=dfs(i+1,'sell')-prices[i]
                case2=dfs(i+1, 'buy')
                dp[(i,status)]=max(case1, case2)
            elif status=='sell':
                case1=dfs(i+2, 'buy')+prices[i]
                case2=dfs(i+1, 'sell')
                dp[(i,status)]=max(case1, case2)
            return dp[(i,status)]
        return dfs(0,'buy')