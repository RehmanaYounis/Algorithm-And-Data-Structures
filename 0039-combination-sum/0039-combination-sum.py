class Solution(object):
    def combinationSum(self, candidates, target):
        res, curSol=[],[]
        curSum=0
        nums=candidates
        length=len(candidates)
        i=0
        def dfs(i,curSum):
            if curSum == target:
                res.append(curSol[:])
                return 
            if curSum> target or i == length:
                return
            dfs(i+1, curSum)
            curSol.append(nums[i])
            dfs(i, curSum+nums[i])
            curSol.pop()
        dfs(0,0)
        return res
            
        
        
        
        