class Solution(object):
    def subsets(self, nums):
        res=[]
        stack=[]
        
        def dfs(i):
            if i>=len(nums):
                res.append(stack[::])
                return 
            stack.append(nums[i])
            dfs(i+1)
            stack.pop()
            dfs(i+1)
        dfs(0)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        res=[]
        subset=[]
        def backTrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backTrack(i+1)
            subset.pop()
            backTrack(i+1)
        backTrack(0)
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
#         subset=[]
        
#         def backtrack(i):
#             if i >= len(nums):
#                 print(subset.copy)
#                 res.append(subset)
#                 return
            
#             subset.append(nums[i])
#             backtrack(i+1)
            
#             subset.pop()
#             backtrack(i+1)
#         backtrack(0)
#         return res