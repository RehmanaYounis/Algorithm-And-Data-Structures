class Solution(object):
    def findMin(self, nums):
        if len(nums)==1: return nums[0]
        l,r=0,len(nums)-1
        while l<r:
            print(nums[l:r+1])
            m=(l+r)//2
            leftVal=nums[l]
            rightVal=nums[r]
            midVal=nums[m]
            if midVal>rightVal:
                l=m+1
            else:
                r=m
        return nums[l]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l,r=0,len(nums)-1
#         curMin=float('inf')
#         while l<r:
#             mid=(l+r)//2
#             curMin=min(curMin, nums[mid])
#             if nums[mid]>nums[r]:
#                 l=mid+1
#             else:
#                 r=mid-1
#         return min(curMin, nums[l])