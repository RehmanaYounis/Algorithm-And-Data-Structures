class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        maxArea=0
        while l<r:
            h=min(height[l], height[r])
            w=r-l
            area=h*w
            maxArea=max(maxArea, area)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxArea