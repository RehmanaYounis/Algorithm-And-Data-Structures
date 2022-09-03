class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=numbers
        l=0
        r=len(nums)-1
        
        while l<r:
            curSum = nums[l]+nums[r]
            if curSum>target:
                r-=1
            elif curSum<target:
                l+=1
            else:
                return [l+1, r+1]