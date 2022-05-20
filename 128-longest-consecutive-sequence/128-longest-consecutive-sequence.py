class Solution(object):
    def longestConsecutive(self, nums):
        numSet=set(nums)
        longest = 0 
        i=0
        while i < len(nums):
            length=0
            if nums[i]-1 not in numSet:
                while (nums[i]+length in numSet ):
                    length+=1
            longest=max(longest, length)
            i+=1
        return longest                
        