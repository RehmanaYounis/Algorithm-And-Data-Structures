class Solution(object):
    def trap(self, height):
        l = 0
        r = len(height)-1
        lMax = height[l]
        rMax=height[r]
        res=0
        while l<r:
            if lMax<rMax:
                l+=1
                lMax=max(lMax, height[l])
                res+=lMax- height[l]
                
            else:
                r-=1
                rMax=max(rMax, height[r])
                res+=rMax- height[r]
                
        return res