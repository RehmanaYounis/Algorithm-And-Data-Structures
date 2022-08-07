class Solution(object):
    def search(self, nums, target):
        l=0
        r=len(nums)-1
        
        while l<=r:
            m=(r+l)//2
            print(m)
            if nums[m]==target:
                return m
            elif target<nums[m]:
                r=m-1
            elif target>nums[m]:
                l=m+1
            print(l,r)
        return -1
            
        
        