class Solution(object):
    def change(self, amount, coins):
        dp={}
        def dfs(j, amount):
            if j>=len(coins):
                return 0
            if (j,amount) in dp:
                return dp[(j,amount)]
            if amount==0:
                return 1
            if amount<0:
                return 0
            dp[(j,amount)] = dfs(j,amount - coins[j]) + dfs(j + 1,amount)
          
            return dp[(j,amount)]
        return dfs(0, amount)
                
        