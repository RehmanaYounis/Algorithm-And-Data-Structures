class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find pivot
        if len(nums) == 1 and target == nums[0]: return 0
        if len(nums) == 1 and target != nums[0]: return -1
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        pivot=l
        l,r=0,len(nums)-1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        print("boundries are", l,r)    
        while l<=r:
            mid=(l+r)//2
            if target == nums[mid]:
                return mid
            elif target >nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l=0
#         r=len(nums)-1
#         mid=(l+r)//2
#         if len(nums)==1:
#             return -1 if not nums[0]==target else 0
#         while l<r:
#             mid=(l+r)//2
#             if nums[l]<nums[mid] and nums[mid] >nums[r]:
#                 l=mid
#             elif nums[l]>nums[mid]  and nums[mid] <nums[r]:
#                 r=mid
#             else:
#                 break
        
#         mid=mid+1
#         print(mid)
#         right=len(nums)-1
#         if target >= nums[mid] and target <= nums[right]:
#             left=mid
            
#         else:
#             left=0
#             right=mid-1
#         l=left
#         r=right
        
#         while l<=r:
#             mid=(l+r)//2
#             if target < nums[mid]:
#                 r=mid-1
#             elif target>nums[mid]:
#                 l=mid+1
#             else:
#                 return mid
#         return -1