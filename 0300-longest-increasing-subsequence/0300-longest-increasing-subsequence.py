class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp={}
        maxLen=1
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if i>=len(nums):
                return 0
            maximum=1
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    # print(nums[i], nums[j])
                    res=1+dfs(j)
                    maximum=max(maximum, res)
            dp[i]=maximum
            return dp[i]
            
        
        
        
        
        for n in range(len(nums)):
            res=dfs(n)
            maxLen=max(maxLen,res)
        return maxLen
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         maxLen=1
#         dp={}
#         def dfs(i):
#             if i in dp:
#                 return dp[i]
#             maxLen=0
#             curVal=nums[i]
#             for j in range(i+1, len(nums)):
#                 if curVal<nums[j]:
#                     maxLen=max(maxLen, dfs(j))
#             dp[i]=maxLen+1
#             return dp[i]
        
#         for i in range(len(nums)):
#             maxLen=max(maxLen,dfs(i))
#         return maxLen
    
        