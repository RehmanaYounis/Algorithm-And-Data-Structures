class Solution(object):
    def twoSum(self, numbers, target):
        nums=numbers
        l=0
        r=len(nums)-1
        while l<r:
            curSum=nums[l]+nums[r]
            if curSum == target:
                return([l+1, r+1])
            if curSum > target:
                r-=1
            else:
                l+=1
                