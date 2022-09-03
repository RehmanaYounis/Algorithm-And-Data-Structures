class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        l=0
        for r in range(1,len(prices)):
            curProf= prices[r]-prices[l]
            maxProfit=max(maxProfit, curProf)
            if prices[l]>prices[r]:
                l=r
        return (maxProfit)