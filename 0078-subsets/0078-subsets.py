class Solution(object):
    def subsets(self, nums):
        res=[]
        visit=[]
        def dfs(i):
            if i == len(nums):
                res.append(visit[:])
                return
            visit.append(nums[i])
            dfs(i+1)
            visit.pop()
            dfs(i+1)
        dfs(0)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
#         def dfs(n, stack):
#             if n>= len(nums):
#                 res.append(stack[::])
#                 return
#             stack.append(nums[n])
#             dfs(n+1, stack)
#             stack.pop()
#             dfs(n+1, stack)
#         dfs(0,[])
#         return res