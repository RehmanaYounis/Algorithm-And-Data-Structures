class Solution(object):
    def coinChange(self, coins, amount):
        dp={}
        def dfs(amount):
            if amount in dp:
                return dp[amount]
            if amount==0:
                return 0
            if amount<0:
                return -1
            minCoin=float('inf')
            for i in coins:
                res=dfs(amount-i)
                if res !=-1:
                    cur=1+res
                    minCoin=min(cur,minCoin)
                    
            dp[amount]=minCoin
            return dp[amount]
        return dfs(amount) if dfs(amount)!= float('inf') else -1
        