class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp={}
        def dfs(n):
            if n in dp:
                return dp[n]
            if n >=len(cost):
                return 0
            case1= cost[n]+dfs(n+1)
            case2=cost[n]+dfs(n+2)
            dp[n]=min(case1, case2)
            return dp[n]
        
        
        return min(dfs(0), dfs(1))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dp={}
#         def dfs(n):
#             if n in dp:
#                 return dp[n]
#             if n>=len(cost):
#                 return 0
#             print(n)
#             case1=cost[n]+dfs(n+1)
#             case2=cost[n]+dfs(n+2)
#             dp[n]=min (case1, case2)
#             return dp[n]
#         return min(dfs(0), dfs(1))