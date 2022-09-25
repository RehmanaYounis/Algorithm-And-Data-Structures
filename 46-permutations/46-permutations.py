class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack=[]
        res=[]
        visit=[]
        def dfs(j, stack):
            
            if len(stack)>=len(nums):
                res.append(stack[::-1])
                return
            for i in range(len(nums)):
                if nums[i] not in visit:
                    visit.append(nums[i])
                    stack.append(nums[i])
                    dfs(i+1,stack)
                    stack.pop()
                    visit.pop()
                
        dfs(0,stack)
        return res