class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countArray=defaultdict(int)
        for num in nums:
            countArray[num]+=1

        freqArray=[[] for i in range(len(nums)+1)]
        for n,c in countArray.items():
            freqArray[c].append(n)
        
        
        res=[]
        for i in range(len(freqArray)-1, 0, -1):
            for elem in freqArray[i]:
                res.append(elem)
                if len(res) == k:
                    return res
        
        
        #  res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res