class Solution(object):
    def sortedSquares(self, nums):
        #1. Find the Middle Element if Array is odd length
        #2. Set left pointer one less that middle
        #3. Set right pointer one greater that middle
        #4. Insert square of the middle in result array
        #5. Loop to add square of left and then square of right in the result array
    
        res=[0 for _ in range(len(nums))]
        index=len(nums)-1
        left=0
        right=len(nums)-1
        
        while left<=right:
            leftSum= nums[left]**2
            rightSum= nums[right]**2
            if leftSum>rightSum:
                res[index]=leftSum
                left+=1
            else:
                res[index]=rightSum
                right-=1
            index-=1
        return res