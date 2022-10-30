class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0:
            return False
        target=sum(nums)//2
        # dp={}
        nums.sort()
        def dfs(target, j):
            if target in dp:
                return dp[target]
            if target ==0:
                return True
            if target <0:
                return False
            
            for i in range(j, len(nums)):
                if dfs(target-nums[i],i+1):
                    dp[target]=True
                    return dp[target]
            dp[target]=False
            return dp[target]
        
        
        for i in range(len(nums)):
            dp={}
            if dfs(target,i):
                return True
        return False
    
    
    
    
   
        
        
            
#             for i in range(j, len(nums)):
#                 if dfs(curSum-nums[i], i+1):
#                     dp[curSum]=True
#                     return True
#             dp[curSum]=False
#             return dp[curSum]
        
#         for i in range(len(nums)):
#             dp={}
#             if dfs(target,i):       
#                 return True
#         return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # return dfs(target,0)
        
        
#         target=sum(nums)%2
#         if target==0:
#             target=sum(nums)//2
#         else:
#             return False
        
#         nums.sort()
#         def dfs(curSum,j):
#             if curSum in dp:
#                 return dp[curSum]
#             if curSum==0:
#                 return True
#             if curSum<0:
#                 return False
#             for i in range(j, len(nums)):
#                 if dfs(curSum-nums[i], i+1):
#                     dp[curSum]=True
#                     return True
#             dp[curSum]=False
#             return dp[curSum]
        
#         for i in range(len(nums)):
#             dp={}
#             if dfs(target,i):       
#                 return True
#         return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         target=sum(nums)%2
#         if target==0:
#             target=sum(nums)//2
#         else:
#             return False
        
#         nums.sort()
#         def dfs(curSum,j):
#             if curSum in dp:
#                 return dp[curSum]
#             if curSum==0:
#                 return True
#             if curSum<0:
#                 return False
#             for i in range(j, len(nums)):
#                 if dfs(curSum-nums[i], i+1):
#                     dp[curSum]=True
#                     return True
#             dp[curSum]=False
#             return dp[curSum]
        
#         for i in range(len(nums)):
#             dp={}
#             if dfs(target,i):       
#                 return True
#         return False