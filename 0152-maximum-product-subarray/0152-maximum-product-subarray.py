class Solution(object):
    def maxProduct(self, nums):
        maxProd, minProd=1,1
        res=max(nums)
        for n in nums:
            temp=maxProd
            maxProd=max(maxProd*n, minProd*n, n)
            minProd=min(minProd*n, temp*n, n)
            res=max(res, maxProd, minProd)
        return res