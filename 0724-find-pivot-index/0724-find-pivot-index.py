class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum=0
        for i in nums:
            totalSum+=i
        left=0
        right=totalSum-nums[0]
        pivot=nums[0]
        for i in range(len(nums)):
            if left==right:
                return i
            left+=nums[i]
            if i+1<len(nums): pivot=nums[i+1]
            right-=pivot
        return -1