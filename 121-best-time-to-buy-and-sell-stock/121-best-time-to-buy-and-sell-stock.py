class Solution(object):
    def maxProfit(self, prices):
        curP, maxP = 0,0
        l, r = 0,1
        while r<len(prices):
            curP= prices[r]-prices[l]
            maxP= max(curP, maxP)
            if prices[l]>prices[r]:
                l=r
                r+=1
            else:
                r+=1
        return maxP
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         cur_prof, max_prof = 0, 0
#         l,r= 0, 1
#         while r <len(prices):
#             cur_prof = prices[r] - prices[l]
#             max_prof = max(max_prof, cur_prof)
#             if prices[l] > prices[r]:
#                 l=r
#                 r=r+1
#             else:
#                 r=r+1
#         return max_prof
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         max_profit=0
#         l=0
#         r = 1
#         for i in range(len(prices)-1):
#             max_profit= max(max_profit, (prices[r]-prices[l])) 
#             if prices[l]>prices[r]:
#                 l=r
#                 r=r+1
#             else:
#                 r=r+1
#         return max_profit
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        
        
        
        
        
        
        
        
        # L= 0
        # R = 1
        # profit = 0
        # while R<len(prices):
        #     if prices[L]> prices[R]:
        #         L=R
        #     profit = max(profit, (prices[R]-prices[L]))
        #     R=R+1
        # return profit