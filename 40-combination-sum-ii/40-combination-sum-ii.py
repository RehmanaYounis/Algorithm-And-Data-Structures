class Solution(object):
    def combinationSum2(self, candidates, target):
        res=[]
        stack=[]
        candidates.sort()
        def dfs(curSum, j):
            if curSum==target:
                res.append(stack[::])
                return
            if curSum>target:
                return
            prev=-1
            for i in range(j,len(candidates)):
                if prev==candidates[i]:
                    continue
                curSum+=candidates[i]
                stack.append(candidates[i])
                dfs(curSum, i+1)
                temp=stack.pop()
                curSum-=temp
                prev=candidates[i]
        dfs(0,0)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
#         stack=[]
#         candidates.sort()

#         def canCombo(cursum, j):
#             if cursum == target:
#                 print(stack, cursum)
#                 if stack not in res:
#                     res.append(stack[::])
#                 return 
#             if  j>=len(candidates) or cursum>target:
#                 return 
#             prev=-1
#             for i in range(j,len(candidates)):
#                 if candidates[i]==prev:
#                     continue
#                 stack.append(candidates[i])
#                 cursum+=candidates[i]
#                 canCombo(cursum, i+1)
#                 e=stack.pop()
#                 cursum-=e
#                 prev=candidates[i]
 

#         canCombo(0,0)
#         return res
        