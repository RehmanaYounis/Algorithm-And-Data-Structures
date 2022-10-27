class Solution(object):
    def maxProfit(self, prices):
        dp={}
        def dfs(i, isBuy):
            if (i, isBuy) in dp:
                return dp[(i, isBuy)]
            if i>=len(prices):
                return 0
            if isBuy=='buy':
                buy=dfs(i+1, 'sell')-prices[i]
                cooldown=dfs(i+1,  'buy')
                res=max(buy,cooldown)
            else:
                sell=dfs(i+2, 'buy')+prices[i]
                cooldown=dfs(i+1, 'sell')
                res=max(sell, cooldown)
            dp[(i, isBuy)]=res
            return dp[(i, isBuy)]
        return dfs(0, 'buy')
        