class Solution(object):
    def longestConsecutive(self, nums):
        numSet= set(nums)
        Longest=0
        for i in nums:
            if (i -1) not in numSet:
                length=0
                while (i+length) in numSet:
                    length+=1
                    Longest=max(Longest, length)
        return Longest