class Solution(object):
    def containsDuplicate(self, nums):
        hashset = {}
        for num in nums:
            if num in hashset:
                return True
            hashset[num]=True
        return False