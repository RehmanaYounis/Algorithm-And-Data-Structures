class Solution(object):
    def subsetsWithDup(self, nums):
        res=[]
        visit=[]
        nums.sort()
        def dfs(i):
            if i == len(nums):
                res.append(visit[:])
                return
            visit.append(nums[i])
            dfs(i+1)
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            visit.pop()
            dfs(i+1)
        dfs(0)
        return res
        
        
        
        
        
        
        
        
        
#         res=[]
#         stack=[]
#         nums.sort()
#         def dfs(i):
#             if i>=len(nums):
#                 res.append(stack[::])
#                 return
            
#             stack.append(nums[i])
#             dfs(i+1)
#             while i+1<len(nums) and nums[i] == nums[i+1]:
#                 i+=1
#             stack.pop()
#             dfs(i+1)
            
# #             stack.append(nums[i])
# #             dfs(i+1)
            
#             stack.pop()
#             while i+1<len(nums) and nums[i] == nums[i+1]:
#                 i+=1
#             dfs(i+1)
        dfs(0)
        return res