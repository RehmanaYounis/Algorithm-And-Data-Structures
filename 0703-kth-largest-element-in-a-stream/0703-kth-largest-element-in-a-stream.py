class KthLargest(object):

    def __init__(self, k, nums):
        self.nums=nums
        heapq.heapify(nums)
        self.k=k
        

    def add(self, val):
        heapq.heappush(self.nums, val)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)