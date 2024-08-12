class Solution(object):
    def combinationSum(self, candidates, target):
        curSum=0
        visit=[]
        res=[]
        nums=candidates
        def dfs(i, curSum):
            if curSum > target or i >= len(nums):
                return
            if curSum== target:
                res.append(visit[:])
                return
            visit.append(nums[i])
            dfs(i, curSum+nums[i])
            visit.pop()
            dfs(i+1, curSum)
        dfs(0, 0)
        return res
            
        
        
        
        
        
#         res=[]
#         curSol=[]
#         def dfs(i, curVal):
#             if i>= len(candidates) or curVal>target:
#                 return
#             if curVal==target:
#                 res.append(curSol[:])
#                 return
#             dfs(i+1, curVal)
#             curSol.append(candidates[i])
#             dfs(i, curVal+candidates[i])
#             curSol.pop()
#         dfs(0,0)
#         return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res, curSol=[],[]
#         curSum=0
#         nums=candidates
#         length=len(candidates)
#         i=0
#         def dfs(i,curSum):
#             if curSum == target:
#                 res.append(curSol[:])
#                 return 
#             if curSum> target or i == length:
#                 return
#             dfs(i+1, curSum)
#             curSol.append(nums[i])
#             dfs(i, curSum+nums[i])
#             curSol.pop()
#         dfs(0,0)
#         return res
            
        
        
        
        