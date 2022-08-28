class Solution:
    def Partition(self, left, right, nums):
        p=left
        pivot=nums[right]
        
        for i in range(left, right):
            if nums[i]<= pivot:
                nums[i],nums[p]=nums[p], nums[i]
                p+=1
        nums[right], nums[p]=nums[p],nums[right]
        return p
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k=len(nums)-k
        left=0
        right=len(nums) -1
        
        while left<right:
            par = self.Partition(left, right, nums)
            if par>k:
                right=par-1
            elif par<k:
                left=par+1
            else:
                break
        return nums[k]
        
        