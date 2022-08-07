class Solution(object):
    def permute(self, nums):
        res=[]
        stack=[]
        used=[False]*len(nums)
        def dfs (j):
            if len(stack) == len(nums):
                res.append(stack[::])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    stack.append(nums[i])
                    dfs(i+1)
                    stack.pop()
                    used[i]=False
        dfs(0)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # nums = [1,2,3]
#         res=[]
#         stack=[]
#         used = [False]*len(nums)
#         def backTrack():
#             if len(stack)==len(nums):
#                 res.append(stack[::])
#                 return

#             for i in range(len(nums)):
#                 if not used[i]:
#                     stack.append(nums[i])
#                     used[i]=True
#                     backTrack()
#                     used[i]=False
#                     stack.pop()
#         backTrack()
#         return res
        