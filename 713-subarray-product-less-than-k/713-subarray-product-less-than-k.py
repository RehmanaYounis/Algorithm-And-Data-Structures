class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curProd=1
        total=0
        subArr=0
        left=0
        for i , val in enumerate(nums):
            curProd*=val
            subArr+=1
            while curProd>=k and left<=i:
                curProd/=nums[left]
                subArr-=1
                left+=1
            if curProd<k:
                total+=subArr
        return total