class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left
            
        for i in range(left, right):
            if nums[i] <= pivot:
                
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
                
        nums[fill], nums[right] = nums[right], nums[fill]
            
        return fill
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1
        
        while left < right:
            pivot = self.partition(nums, left, right)
            
            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nums = [-s for s in nums]
#         heapq.heapify(nums)
       
#         print(nums)
#         n=1
#         while n <k:
#             heapq.heappop(nums)
#             n+=1
#         return -(heapq.heappop(nums))