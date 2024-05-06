class Solution(object):
    def maxProfit(self, prices):
        l,r=0,1
        maxProf,currProf = 0,0
        while r < len(prices):
            if prices[l] <prices[r]:
                currProf=prices[r]-prices[l]
                maxProf=max(currProf, maxProf)
            else:
                l=r
            r+=1
        return maxProf
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l=0
#         r=1
#         maxProfit=0
#         nums=prices
#         while r<len(nums):
#             curProfit = nums[r]-nums[l]
#             maxProfit = max(maxProfit , curProfit)
#             if nums[l]>nums[r]:
#                 l=r
#             r=r+1
#         return maxProfit