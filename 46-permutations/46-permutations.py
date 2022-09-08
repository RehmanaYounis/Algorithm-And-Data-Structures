class Solution(object):
    def permute(self, nums):
        res=[]
        stack=[]
        visit=set()
        
        def dfs():
            if len(stack)==len(nums):
                res.append(stack[:])
                return
            for i in nums:
                if i not in visit:
                    visit.add(i)
                    stack.append(i)
                    dfs()
                    stack.pop()
                    visit.remove(i)
        dfs()
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
        