class Solution(object):
    def search(self, nums, target):
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        mid=l
        l=0
        r=len(nums)-1
        if target >= nums[mid] and target <= nums[r]:
            l=mid
        else:
            r=mid
        while l<=r:
            mid =(l+r)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid -1
        return -1
        