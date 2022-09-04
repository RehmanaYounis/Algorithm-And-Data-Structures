class Solution(object):
    def trap(self, height):
        l=0
        r=len(height)-1
        maxLeft=height[l]
        maxRight=height[r]
        res=0
        
        while l<r:
            if maxLeft <maxRight:
                l+=1
                maxLeft=max(maxLeft, height[l])
                res+= maxLeft-height[l]
                
            else:
                r-=1
                maxRight=max(maxRight, height[r])
                res+= maxRight-height[r]
              
        return res
                   