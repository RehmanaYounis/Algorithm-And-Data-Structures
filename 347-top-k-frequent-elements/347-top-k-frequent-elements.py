class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap={}
        for i in nums:
            hashmap[i]=1+hashmap.get(i, 0)
        
        countArray=[]
        for i in range(len(nums)+1):
            countArray.append([])
        
        
        for key, value in hashmap.items():
            countArray[value].append(key)
        
        result=[]
        for i in range(len(countArray)-1, 0, -1):
            for values in countArray[i]:
                result.append(values)
                if len(result)==k:
                    return result