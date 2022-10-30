class Solution(object):
    def lengthOfLIS(self, nums):
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >=len(nums):
                return 0
            maxLen=1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    cur=1+dfs(j)
                    maxLen=max(maxLen, cur)
            dp[i]=maxLen
            return dp[i]
        
        maxLen=1
        dp={}
        for i in range(len(nums)):  
            maxLen=max(maxLen, dfs(i))
        return maxLen
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         maxLen=1
#         dp={}
#         def dfs(i):
#             if i in dp:
#                 return dp[i]
#             maxLen=0
#             for j in range(i+1, len(nums)):
#                 if nums[i]<nums[j]:
#                     cur=dfs(j)
#                     maxLen=max(maxLen,cur )
#             dp[i]=maxLen+1
#             return dp[i]
        
#         for i in range(len(nums)):
#             maxLen=max(maxLen,dfs(i))
#         return maxLen
    