class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res=[]
        stack=[]
        def dfs(i):
            if i>= len(nums):
                res.append(stack[::-1])
                return
            stack.append(nums[i])
            dfs(i+1)
            stack.pop()
            while i+1< len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res
        