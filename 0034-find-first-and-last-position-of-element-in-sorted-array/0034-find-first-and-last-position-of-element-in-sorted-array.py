class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bsearch(l,r,dire):
            i=-1
            while l<=r:
                m=(l+r)//2
                if target>nums[m]:
                    l=m+1
                elif target <nums[m]:
                    r=m-1
                else:
                    i=m
                    if dire =='left':
                        r=m-1
                    else:
                        l=m+1
            return i
                
        left=bsearch(0,len(nums)-1,'left')
        right= bsearch(0,len(nums)-1,'right')
        return [left,right]
                        