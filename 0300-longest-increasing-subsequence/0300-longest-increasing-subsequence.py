class Solution(object):
    def lengthOfLIS(self, nums):
        
#         def dfs(i):
#             if i>=len(nums):
#                 return 0
            
#             res=0
#             for j in range(i, len(nums)):
#                 if j+1< len(nums) and nums[j]<nums[j+1]:
#                     cur=1+dfs(j+1)
#                     res=max(res,cur)
#                     print(j, res)
#             return res
#         dfs(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        maxLen=1
        dp={}
        def dfs(i):
            if i in dp:
                return dp[i]
            maxLen=0
            curVal=nums[i]
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    maxLen=max(maxLen, dfs(j))
            dp[i]=maxLen+1
            return dp[i]
        
        for i in range(len(nums)):
            maxLen=max(maxLen,dfs(i))
        return maxLen
    