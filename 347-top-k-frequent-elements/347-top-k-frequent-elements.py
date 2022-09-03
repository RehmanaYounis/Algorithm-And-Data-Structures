class Solution(object):
    def topKFrequent(self, nums, k):
        CMap=Counter(nums)
        res=[]
        for val in CMap:
            heapq.heappush(res, [-CMap[val], val])
        final=[]
        while k>0:
            _,val = heapq.heappop(res)
            final.append(val)
            k-=1
        return final
        