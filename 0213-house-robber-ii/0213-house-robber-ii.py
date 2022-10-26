class Solution(object):
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        def out_rob(nums):
                dp1={}
                dp2={}
                return max(dfs(0,nums[1:],dp1), dfs(0,nums[:-1],dp2))
        
        def dfs(n,nums,dp):
            if n in dp:
                return dp[n]
            if n>=len(nums):
                return 0
            case1=nums[n]+dfs(n+2, nums,dp)
            case2=dfs(n+1, nums,dp)
            dp[n]=max(case1,case2)
            return dp[n]
        return out_rob(nums)
        