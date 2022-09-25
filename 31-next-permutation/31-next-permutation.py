class Solution(object):
    def nextPermutation(self, nums):
        index=len(nums)-2
        start=0
        
        while index>=0 and nums[index]>=nums[index+1]:
            index-=1
            
        # Find the first elements on the left side greater than current index val
        if index>=0:
            right=len(nums)-1
            while nums[right]<=nums[index] and right>0:
                right-=1
            # right-=1
            nums[index],nums[right]=nums[right],nums[index]
            start = index+1
        # Reverse elements of left part starting from index +1
        
        end=len(nums)-1
        while start<end:
            nums[start], nums[end]=nums[end],nums[start]
            start+=1
            end-=1
        return nums
            