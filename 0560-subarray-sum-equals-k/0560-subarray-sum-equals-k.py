class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap=defaultdict(int)
        sumMap[0]=1
        curSum=0
        res=0
        for num in nums:
            curSum+=num
            diff=curSum-k
            res+=sumMap[diff]
            sumMap[curSum]+=1
        return res