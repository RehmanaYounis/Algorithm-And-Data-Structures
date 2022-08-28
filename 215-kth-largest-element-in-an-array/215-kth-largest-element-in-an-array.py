class Solution(object):
    def Partition(self, left, right, nums):
        p=left
        pivot =nums[right]
        for i in range(left, right):
            if nums[i]<=pivot:
                nums[i],nums[p]=nums[p], nums[i]
                p+=1
        nums[p], nums[right]=nums[right], nums[p]
        return p
    
    
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums)-1
        k=len(nums)-k
        while left<right:
            p = self.Partition(left, right, nums)
            if p>k:
                right=p-1
            elif p<k:
                left=p+1
            else:
                break
        return nums[k]
        
        
    

