class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap=Counter(nums)
        freqList=[[] for i in range (len(nums)+1)]
        for key, val in countMap.items():
            freqList[val].append(key)
        res=[]
        for i in reversed(range(len(freqList))):
            if freqList[i]:
                for val in freqList[i]:
                    res.append(val)
                    if len(res) == k:
                        return res
         
        
        
        
        