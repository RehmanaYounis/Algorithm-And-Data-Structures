class Solution(object):
    def lengthOfLIS(self, nums):
        dp={}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >=len(nums):
                return 0
            curMax=1
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    cur=1+dfs(j)
                    curMax=max(curMax, cur)
                    # return curMax
            dp[i]=curMax
            return dp[i]
        maxLen=1
        for i in range(len(nums)):
           
            maxLen=max(maxLen, dfs(i))
        return maxLen
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def dfs(i):
#             if i in dp:
#                 return dp[i]
#             if i >=len(nums):
#                 return 0
#             maxLen=1
#             for j in range(i+1,len(nums)):
#                 if nums[i]<nums[j]:
#                     cur=1+dfs(j)
#                     maxLen=max(maxLen, cur)
#             dp[i]=maxLen
#             return dp[i]
        
#         maxLen=1
#         dp={}
#         for i in range(len(nums)):  
#             maxLen=max(maxLen, dfs(i))
#         return maxLen
       
        
        
        
        
        
        
        
        
        
        
        
        
        
