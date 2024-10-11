class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preMap=defaultdict(int)
        preMap[0]=1
        curSum=0
        res=0
        for num in nums:
            curSum +=num
            diff=curSum-k
            res+=preMap[diff]
            preMap[curSum]+=1
        return res