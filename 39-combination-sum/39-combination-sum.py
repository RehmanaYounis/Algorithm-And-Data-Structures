class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        stack=[]
        def calSum(j, curSum):
            if curSum==target:
                res.append(stack[::])
                return
            elif curSum>target:
                return
            for i in range(j, len(candidates)):
                stack.append(candidates[i])
                calSum(i, curSum+candidates[i])
                stack.pop()
        calSum(0,0)
        return res
        