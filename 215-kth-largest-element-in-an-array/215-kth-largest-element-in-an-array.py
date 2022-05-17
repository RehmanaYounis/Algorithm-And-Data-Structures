class Solution(object):
    def findKthLargest(self, nums, k):
        a=sorted(nums)
        return (a[len(nums)-k])