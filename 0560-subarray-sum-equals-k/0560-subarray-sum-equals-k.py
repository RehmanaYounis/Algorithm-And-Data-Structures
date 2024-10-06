class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum=0
        preMap={0:1}
        res=0
        for n in nums:
            curSum+=n
            diff =curSum -k
            res += preMap.get(diff,0)
            preMap[curSum] = 1+preMap.get(curSum,0)
        return res
            
            
        