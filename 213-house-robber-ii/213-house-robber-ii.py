class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
                return nums[0]
        def RobHelper(nums):
            print(nums)
            n=len(nums)
            
            if not nums: return 0
            if len(nums)<3:
                return max(nums)
            elif len(nums)==3:
                return max(nums[n-3]+nums[n-1], nums[1])

            nums[n-3]=nums[n-3]+nums[n-1]
            for i in range(n-4, -1, -1):
                nums[i]=max(nums[i]+nums[i+2], nums[i]+nums[i+3])
            print(nums)
            
            print( max(nums[0], nums[1]))
            return max(nums[0], nums[1])
        
        return max(RobHelper(nums[1:len(nums)]), RobHelper(nums[:len(nums)-1]))