class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap=defaultdict(int)
        for i in nums:
            countMap[i]+=1
        lst=[[] for i in range(len(nums) + 1)]
        
        for key,val in countMap.items():
            lst[val].append(key)
        res=[]
        for i in range(len(lst) - 1, 0, -1):
            for j in range(len(lst[i])):
                res.append(lst[i][j])
                if len(res)==k:
                    return res