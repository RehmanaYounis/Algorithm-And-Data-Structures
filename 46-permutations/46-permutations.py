class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[]
        visit=[]
        def perm():
            if len(stack) == len(nums):
                res.append(stack[::])
                return
            for i in range(len(nums)):
                if nums[i] not in visit:
                    visit.append(nums[i])
                    stack.append(nums[i])
                    perm()
                    stack.pop()
                    visit.pop()
            
        perm()
        return res