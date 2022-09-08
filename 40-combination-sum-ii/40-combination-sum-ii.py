class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack=[]
        res=[]
        nums=candidates
        nums.sort()
        def dfs(j, curSum):
            if curSum>target:
                return
            if curSum==target:
                res.append(stack[:])
                return
            prev=-1
            for i in range(j, len(nums)):
                if prev == nums[i]:
                    continue
                stack.append(nums[i])
                dfs(i+1,curSum+nums[i])
                stack.pop()
                prev=nums[i]
        dfs(0,0)
        return res
    
    
   