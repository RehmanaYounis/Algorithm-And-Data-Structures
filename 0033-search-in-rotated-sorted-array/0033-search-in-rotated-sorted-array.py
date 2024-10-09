# [4,5,6,7,0,1,2]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot point
        if len(nums) ==0: return -1
        l,r=0, len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid] > nums[r]:
                l=mid+1
            else:
                r=mid
            
        pivot=l
        l,r=0, len(nums)-1
        if target >=nums[pivot] and target <=nums[r]:
            l=pivot
        elif target >= nums[l] and target <=nums[pivot-1]:
            r=pivot-1
        print(l,r)
        while l<=r:
            mid=(l+r)//2
            if target < nums[mid]:
                r=mid-1
            elif target >nums[mid]:
                l=mid+1
            else:
                return mid
        return -1
            
                
# if len(nums) == 1 and target == nums[0]: return 0
#         if len(nums) == 1 and target != nums[0]: return -1
#         l,r=0,len(nums)-1
#         while l<r:
#             mid=(l+r)//2
#             if nums[mid]>nums[r]:
#                 l=mid+1
#             else:
#                 r=mid
#         pivot=l
#         l,r=0,len(nums)-1
#         if target >= nums[pivot] and target <= nums[r]:
#             l = pivot
#         else:
#             r = pivot - 1
#         print("boundries are", l,r)    
#         while l<=r:
#             mid=(l+r)//2
#             if target == nums[mid]:
#                 return mid
#             elif target >nums[mid]:
#                 l=mid+1
#             else:
#                 r=mid-1
#         return -1