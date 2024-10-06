class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        maxProf=0
        while r< len(prices):
            if prices[r] < prices[l]:
                l=r
            maxProf=max(maxProf, (prices[r]-prices[l]))
            r+=1
        return maxProf
            