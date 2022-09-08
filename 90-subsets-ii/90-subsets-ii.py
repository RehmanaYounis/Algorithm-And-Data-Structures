class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        subset=[]
        def backTrack(i):
            if i>=len(nums):
                if subset not in res:
                    res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backTrack(i+1)
            subset.pop()
            backTrack(i+1)
        backTrack(0)
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def backTrack(i):
#             if i>=len(nums):
#                 if subset not in res:
#                     res.append(subset.copy())
#                 return
            
#             subset.append(nums[i])
#             backTrack(i+1)
#             subset.pop()
#             backTrack(i+1)
#         backTrack(0)
#         return res
            