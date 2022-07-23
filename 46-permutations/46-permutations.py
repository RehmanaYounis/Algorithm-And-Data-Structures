class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        
        def backTrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    perm.append(nums[i])
                    backTrack(perm)
                    used[i]=False
                    perm.pop()
        backTrack([])
        return res
            