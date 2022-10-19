class Solution(object):
    def findDisappearedNumbers(self, nums):
        hashMap=defaultdict(int)
        for i in nums:
            hashMap[i]+=1
        res=[]
        for i in range(1,len(nums)+1):
            if i not in hashMap:
                res.append(i)
        return res