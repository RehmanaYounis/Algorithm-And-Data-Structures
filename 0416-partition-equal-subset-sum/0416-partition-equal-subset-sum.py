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
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if sum(nums)%2 !=0:
#             return False
#         target=sum(nums)//2
#         dp={}
#         nums.sort()
#         def dfs(target, j):
#             if (target, j) in dp:
#                 return dp[(target, j)]
#             if target ==0:
#                 return True
#             if target <0:
#                 return False
#             dp[(target,j)]=False
#             for i in range(j, len(nums)):
#                 if dfs(target-nums[j],i+1):
#                     dp[(target,j)]=True
#                     return dp[(target,j)]
            
#             return dp[(target,j)]
#             return False
#         return dfs(target,0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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