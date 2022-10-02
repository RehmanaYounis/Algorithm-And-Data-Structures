class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        stack=[]
        # target=7
        def combSum(curSum, j):
            if curSum>target:
                return
            if curSum== target:
                res.append(stack[::])
                return
            for i in range(j, len(candidates)):
                    stack.append(candidates[i])
                    curSum+=candidates[i]
                    combSum(curSum, i)
                    temp=stack.pop()
                    curSum-=temp
        combSum(0,0)
        return res