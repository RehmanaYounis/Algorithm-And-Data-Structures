class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum=0
        preMap=defaultdict(int)
        preMap[0]=1
        res=0
        for n in nums:
            curSum+=n
            diff =curSum -k
            res += preMap[diff]
            preMap[curSum] = 1+preMap[curSum]
        return res
            
            
        