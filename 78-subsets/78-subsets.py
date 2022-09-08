class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack=[]
        res=[]
        def dfs(i):
            if i ==len(nums):
                res.append(stack[::-1])
                return
            stack.append(nums[i])
            dfs(i+1)
            stack.pop()
            dfs(i+1)
        dfs(0)
        return res