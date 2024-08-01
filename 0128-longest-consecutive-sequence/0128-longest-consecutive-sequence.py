class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        maxLen=0
        
        for num in nums:
            if (num-1) not in numSet:
                length=1
                while (num+length) in numSet:
                    length+=1
                maxLen=max(length, maxLen)
        return maxLen
            