class Solution(object):
    def removeElement(self, nums, val):
        left=0
        right= 0
        while right<len(nums):
            if nums[right] != val:
                nums[left]=nums[right]
                left+=1
                
                
            right+=1
        print(nums)
        return left
        