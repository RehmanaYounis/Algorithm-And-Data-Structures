class Solution(object):
    def combinationSum2(self, candidates, target):
        nums=candidates
        nums.sort()
        res=[]
        stack=[]
        def dfs(j, curSum):
            if curSum==target:
                res.append(stack[::])
                return
            if curSum>target:
                return
            prev=-1
            for i in range(j,len(nums)):
                if prev == nums[i]:
                    continue
                stack.append(nums[i])
                dfs(i+1, curSum+nums[i])
                stack.pop()
                prev=nums[i]
        dfs(0, 0)
        return res
                
        