class Solution(object):
    def search(self, nums, target):
        left = 0; right = len(nums)-1
        #Find Element that divides array into two sorted part
        mid=left
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right=mid
        mid=left
        left = 0; right = len(nums)-1
        if target>=nums[mid] and target<=nums[right]:
            left=mid
        else:
            right = mid
        
        while left<=right:
            mid=(left+right)//2
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return -1