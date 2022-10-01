class Solution(object):
    def subsets(self, nums):
        res=[]
        stack=[]
        def dfs(i):
            if i>= len(nums):
                res.append(stack[::-1])
                return
            stack.append(nums[i])
            dfs(i+1)
            stack.pop()
            dfs(i+1)
        dfs(0)
        return res