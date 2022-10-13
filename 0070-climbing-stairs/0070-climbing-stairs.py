class Solution:
    def climbStairs(self, n: int) -> int:
        count=0
        sMap=defaultdict(int)
        def dfs(n):
            if n<=1:
                return 1
            if n in sMap:
                return sMap[n]
            withOne=dfs(n-1)
            withTwo=dfs(n-2)
            sMap[n]=withOne+withTwo
            return withOne+withTwo
        return dfs(n)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # one, two= 1,1
        # for i in range(n-1):
        #     temp=one
        #     one +=two
        #     two = temp
        # return one