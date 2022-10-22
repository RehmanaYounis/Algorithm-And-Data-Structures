class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        nums=candidates
        stack=[]

        def dfs(j, curSum):
            if curSum==0:
                return True
            if curSum<0:
                return False
            for i in range(j, len(candidates)):
                stack.append(nums[i])
                if dfs(i, curSum-nums[i]):
                    res.append(stack[::])
                stack.pop()
        dfs(0,target)
        return res
            