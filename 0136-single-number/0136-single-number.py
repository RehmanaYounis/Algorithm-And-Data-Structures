# We are using XOR, when XOR see a number for first time it adds that to result, 
# and when a number reappeared that value gets subtracted, and at the end only the
# non repetative value would remain in result

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res ^= i
        return res