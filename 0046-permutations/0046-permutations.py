class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visit=[]
        def dfs():
            if len(visit)==len(nums):
                res.append(visit[:])
                return
            for i in nums:
                if i not in visit:
                    visit.append(i)
                    dfs()
                    visit.pop()
        dfs()
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
#         visit=[]
#         def dfs():
#             if len(visit) ==len(nums):
#                 res.append(visit[:])
#                 return
#             for i in nums:
#                 if i not in visit:
#                     visit.append(i)
#                     dfs()
#                     visit.pop()
#         dfs()
#         return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
#         stack=[]
#         def dfs():
#             if len(stack)==len(nums):
#                 res.append(stack[::])
#                 return
            
#             for i in nums:
#                 if i not in stack:
#                     stack.append(i)
#                     dfs()
#                     stack.pop()
#         dfs()
#         return res    
    
    