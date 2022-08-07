class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        stack=[]
        def dfs(curSum, j):
            if curSum==target:
                res.append(stack[::])
                return
            if curSum>target:
                return
            for i in range(j,len(candidates)):
                curSum+=candidates[i]
                stack.append(candidates[i])
                dfs(curSum, i)
                temp=stack.pop()
                curSum-=temp
        dfs(0,0)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
#         stack=[]
#         def combSum(curSum, j):
#             if curSum>target:
#                 return
#             if curSum== target:
#                 res.append(stack[::])
#                 return
#             for i in range(j, len(candidates)):
#                     stack.append(candidates[i])
#                     curSum+=candidates[i]
#                     combSum(curSum, i)
#                     temp=stack.pop()
#                     curSum-=temp
#         combSum(0,0)
#         return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         output=[]
#         subset=[]
#         def backTrack(i, total):
#             if i >=len(candidates) or total>target:
#                 return
#             if total == target:
#                 print(subset)
#                 output.append(subset.copy())
#                 return
#             subset.append(candidates[i])
#             backTrack(i, total+candidates[i])
            
#             subset.pop()
#             backTrack(i+1, total)
            
#         backTrack(0, 0)
#         return output
    