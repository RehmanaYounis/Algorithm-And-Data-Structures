class Solution(object):
    def subsets(self, nums):
        res=[]
        def dfs(i,stack):
            if i >=len(nums):
                res.append(stack[::])
                return
            stack.append(nums[i])
            dfs(i+1, stack)
            stack.pop()
            dfs(i+1, stack)
        dfs(0,[])
        return res
        