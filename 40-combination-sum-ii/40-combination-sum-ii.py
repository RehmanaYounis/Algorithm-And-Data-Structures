class Solution(object):
    def combinationSum2(self, candidates, target):
        res=[]
        stack=[]
        candidates.sort()
        def dfs(curSum,j):
            if curSum==target:
                res.append(stack[::-1])
                return 
            if curSum>target:
                return
            prev=-1
            for i in range(j,len(candidates)):
                if prev == candidates[i]:
                    continue
                stack.append(candidates[i])
                dfs(curSum+candidates[i], i+1)
                stack.pop()
                prev=candidates[i]
        dfs(0,0)
        return res
        