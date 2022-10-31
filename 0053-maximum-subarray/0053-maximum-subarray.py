class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=max(nums)
        l=0
        r=0
        while r<len(nums):
            cur=0
            while r<len(nums) and cur>=0:
                # print(r, nums[r], cur)
                cur+=nums[r]
                r+=1
                maxSum=max(maxSum, cur)
            l=r
        return maxSum
            