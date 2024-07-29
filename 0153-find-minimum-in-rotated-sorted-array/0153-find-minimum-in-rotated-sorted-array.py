class Solution(object):
    def findMin(self, nums):
        l,r=0,len(nums)-1
        curMin=float('inf')
        while l<r:
            mid=(l+r)//2
            curMin=min(curMin, nums[mid])
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
        return min(curMin, nums[l])