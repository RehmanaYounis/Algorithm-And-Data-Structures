class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        stack=[]
        def dfs(i, curSum):
            if curSum==target:
                res.append(stack.copy())
                print(res)
                return
            if i>=len(candidates) or curSum>target:
                return
            
            
            stack.append(candidates[i])
            dfs(i, curSum+candidates[i])
            stack.pop()
            dfs(i+1, curSum)
        dfs(0,0)
        return res
   