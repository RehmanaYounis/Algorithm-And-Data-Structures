class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def backTrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backTrack(i+1)
            subset.pop()
            backTrack(i+1)
        backTrack(0)
        return res
            
        
        