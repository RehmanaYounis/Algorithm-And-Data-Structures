class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)%2
        if target==0:
            target=sum(nums)//2
        else:
            return False
        
        nums.sort()
        def dfs(curSum,j):
            if curSum in dp:
                return dp[curSum]
            if curSum==0:
                return True
            if curSum<0:
                return False
            for i in range(j, len(nums)):
                if dfs(curSum-nums[i], i+1):
                    dp[curSum]=True
                    return True
            dp[curSum]=False
            return dp[curSum]
        
        for i in range(len(nums)):
            dp={}
            if dfs(target,i):       
                return True
        return False