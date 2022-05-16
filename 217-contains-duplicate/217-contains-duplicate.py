class Solution(object):
    def containsDuplicate(self, nums):
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=True
            else:
                return True
        return False
        