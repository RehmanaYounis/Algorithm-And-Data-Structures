class Solution(object):
    def climbStairs(self, n):
        sMap=defaultdict(int)
        def dfs(n):
            if n <=1:
                return 1
            
            if n in sMap:
                return sMap[n]
            sMap[n]=dfs(n-1)+dfs(n-2)
            return sMap[n]
        return dfs(n)