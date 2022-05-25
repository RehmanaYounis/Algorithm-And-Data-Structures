class Solution(object):
    def trap(self, height):
        l, r = 0, len(height)-1
        lMax, rMax = height[l], height[r]
        result=0
        while l<r:
            if lMax < rMax:
                l+=1
                lMax=max(lMax, height[l])
                result+=lMax-height[l]
            else:
                r-=1
                rMax=max(rMax, height[r])
                result+=rMax-height[r]
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     l, r =0 , len(height)-1
#         lmax , rmax = height[l], height[r]
#         res = 0
        
#         while l<r:
#             if lmax<rmax:
#                 l =l+1
#                 lmax = max(lmax, height[l])
#                 res = res + (lmax-height[l])
#             else:
#                 r =r -1
#                 rmax = max(rmax, height[r])
#                 res = res + (rmax-height[r])
#         return res
        