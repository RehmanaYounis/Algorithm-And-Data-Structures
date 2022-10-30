class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0:
            return False
        target=sum(nums)//2
        nums.sort()
        def dfs(target, j):
            if target in dp:
                return dp[target]
            if target ==0:
                return True
            if target <0:
                return False
            dp[target]=False
            for i in range(j, len(nums)):
                if dfs(target-nums[i],i+1):
                    dp[target]=True
                    return dp[target]
            
            return dp[target]
            return False
        
        
        for i in range(len(nums)):
            dp={}
            if dfs(target,i):
                return True
        return False
    
    
    