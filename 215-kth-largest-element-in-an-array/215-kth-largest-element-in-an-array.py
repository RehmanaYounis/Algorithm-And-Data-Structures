class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
       
        print(nums)
        n=1
        while n <k:
            heapq.heappop(nums)
            n+=1
        return -(heapq.heappop(nums))