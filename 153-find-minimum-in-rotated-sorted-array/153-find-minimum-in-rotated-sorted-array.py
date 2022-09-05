class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right = len(nums)-1
        if nums[left]<=nums[right]:
            return nums[left]
        while left<right:
            pivot = (left+right)//2
            if nums[left]>nums[pivot] and nums[pivot]<nums[right]:
                right=pivot
            elif nums[left]<nums[pivot] and nums[pivot]>nums[right]:
                left=pivot
            else:
                break
                
        
        pivot=pivot+1
        return nums[pivot]    
    
   