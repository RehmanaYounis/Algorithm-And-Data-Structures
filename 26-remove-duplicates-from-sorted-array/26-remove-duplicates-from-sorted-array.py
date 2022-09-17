class Solution(object):
    def removeDuplicates(self, nums):
        left=1
        right=1
        arr=nums
        while right<len(arr):
            while arr[right]==arr[right-1] and right<len(arr)-1:
                right+=1
            if (arr[right]!= arr[right-1]):
                arr[left]=arr[right]
                left+=1
            right+=1
        
        return left