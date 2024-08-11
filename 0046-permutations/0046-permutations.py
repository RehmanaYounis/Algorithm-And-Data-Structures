class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[]
        visit=[]
        def dfs():
            if len(stack)==len(nums):
                res.append(stack[::])
                return
            
            for i in nums:
                if i not in stack:
                    stack.append(i)
                    dfs()
                    stack.pop()
        dfs()
        return res    
    
    