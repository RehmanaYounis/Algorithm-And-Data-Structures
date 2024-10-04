class Solution(object):
    def maxProfit(self, prices):
        l,r=0,1
        maxProf=0
        nums=prices
        while r<len(prices):
            curProf=nums[r]-nums[l]
            maxProf=max(maxProf,curProf)
            if nums[r]<nums[l]:
                l=r
                r+=1
            else:
                r+=1
        return maxProf
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l=0
#         r=1
#         maxProfit=0
#         while r<len(prices):
#             curProf=prices[r]-prices[l]
#             maxProfit=max(maxProfit,curProf)
#             if prices[r]<prices[l]:
#                 l=r
#                 r+=1
#             else:
#                 r+=1
#         return maxProfit
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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