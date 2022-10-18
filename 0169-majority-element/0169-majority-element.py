class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap=defaultdict(int)
        for num in nums:
            hashMap[num]+=1
        for key in hashMap:
            if hashMap[key] > len(nums)/2:
                return key
       