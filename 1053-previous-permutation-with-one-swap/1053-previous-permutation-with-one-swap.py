
class Solution(object):
    def prevPermOpt1(self, arr):
        n=len(arr)-1
        nums=arr
        left=n
        while left >= 0 and nums[left] >= nums[left-1]:
            left -= 1
        
        
        if left <= 0:
            return nums

        k = left - 1

        right = n
        while right >= left:
            if nums[right] < nums[k] and nums[right] != nums[right-1]:
                nums[k], nums[right] = nums[right], nums[k]
                return nums

            right -= 1

        return nums