class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin=1,1
        res=max(nums)
        for n in nums:
            temp=curMax
            curMax=max(n, n*curMax, n*curMin)
            curMin=min(n,n*temp, n*curMin)
            res=max(res, curMax,curMin)
        return res