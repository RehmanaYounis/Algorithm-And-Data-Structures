class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0: return -1
        l=0 ; r=len(nums)-1
        mid=l
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        mid=l
        l=0 ; r=len(nums)-1
        
        if target >= nums[mid] and target <= nums[r]:
            l=mid
        else:
            r=mid
        
        while l<=r:
            mid =(l+r)//2
            if target==nums[mid]:
                return mid
            if target>=nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1
        
                