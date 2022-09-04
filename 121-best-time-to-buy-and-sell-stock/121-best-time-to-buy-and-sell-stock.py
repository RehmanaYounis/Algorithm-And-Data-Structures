class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        maxProfit=0
        nums=prices
        while r<len(nums):
            curProfit = nums[r]-nums[l]
            maxProfit = max(maxProfit , curProfit)
            if nums[l]>nums[r]:
                l=r
            r=r+1
        return maxProfit