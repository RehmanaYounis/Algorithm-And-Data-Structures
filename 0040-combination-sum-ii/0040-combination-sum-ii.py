class Solution(object):
    def combinationSum2(self, candidates, target):
        res=[]
        candidates.sort()
        stack=[]
        def dfs(j,curSum):
            if curSum==0:
                res.append(stack[::])
                return
            if curSum<0:
                return 
            prev=-1
            for i in range(j, len(candidates)):
                if prev != candidates[i]:
                    stack.append(candidates[i])
                    dfs(i+1, curSum-candidates[i])
                    stack.pop()
                prev=candidates[i]
        dfs(0,target)
        return res