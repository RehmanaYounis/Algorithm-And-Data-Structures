class Solution(object):
    def subsets(self, nums):
        res=[]
        def dfs(n, stack):
            if n>= len(nums):
                res.append(stack[::])
                return
            stack.append(nums[n])
            dfs(n+1, stack)
            stack.pop()
            dfs(n+1, stack)
        dfs(0,[])
        return res