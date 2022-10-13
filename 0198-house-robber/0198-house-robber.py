class Solution:
    def rob(self, nums: List[int]) -> int:
        rMap=defaultdict(int)
        def helper(n):
            if n==0:
                return nums[0]
            if n<0:
                return 0
            if n in rMap:
                return rMap[n]
            choice1= nums[n]+helper(n-2)
            choice2= helper(n-1)
            rMap[n]=max(choice1, choice2)
            return max(choice1, choice2)
        
        return helper(len(nums)-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n=len(nums)
#         if len(nums)<3:
#             return max(nums)
#         elif len(nums)==3:
#             return max(nums[n-3]+nums[n-1], nums[1])
       
#         nums[n-3]=nums[n-3]+nums[n-1]
#         for i in range(n-4, -1, -1):
#             nums[i]=max(nums[i]+nums[i+2], nums[i]+nums[i+3])
#         print(nums)
#         return max(nums[0], nums[1])