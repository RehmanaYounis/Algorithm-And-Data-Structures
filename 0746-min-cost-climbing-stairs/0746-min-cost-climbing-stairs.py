class Solution(object):
    def minCostClimbingStairs(self, cost):
        hashMap={}
        def dfs(n):
            if n>=len(cost):
                return 0
            if n in hashMap:
                return hashMap[n]
            withOneStep=cost[n]+dfs(n+1)
            withTwoStep=cost[n]+dfs(n+2)
            hashMap[n]=min(withOneStep, withTwoStep)
            return hashMap[n]
        return min(dfs(0), dfs(1))