class Solution(object):
    def moveZeroes(self, nums):
        l,r=0,0
        while l<len(nums) and r <len(nums):
            if nums[r] !=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1