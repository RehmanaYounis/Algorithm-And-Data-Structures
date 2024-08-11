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
                    visit.append(i)
                    stack.append(i)
                    dfs()
                    visit.pop()
                    stack.pop()
        dfs()
        return res    
    
    