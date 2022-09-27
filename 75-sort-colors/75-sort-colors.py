class Solution(object):
    def sortColors(self, nums):
        left=0
        mid=0
        right=len(nums)-1
        arr=nums
        while mid<=right:
            if arr[mid]==0:
                arr[mid], arr[left]=arr[left],arr[mid]
                left+=1
                mid+=1
            elif arr[mid]==2:
                arr[mid], arr[right]=arr[right],arr[mid]
                right-=1
            else:
                mid+=1
        return nums
        