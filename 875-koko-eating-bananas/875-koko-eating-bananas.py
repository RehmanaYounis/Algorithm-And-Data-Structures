class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right= 1, max(piles)
        mink=max(piles)
        while left<=right:
                mid= (left+right)//2
                res=0
                for pile in piles:
                    res+= math.ceil( pile/mid)
                if   res<= h:
                    mink = min(mink, mid)
                    right=mid -1
                else:
                    
                    left = mid+1
                    
        return mink
            