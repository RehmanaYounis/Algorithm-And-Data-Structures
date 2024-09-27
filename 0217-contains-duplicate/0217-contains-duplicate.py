class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap=defaultdict(int)
        for i in nums:
            hmap[i]+=1
            if hmap[i]>1:
                return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
#         hashmap={}
#         for num in nums:
#             if num in hashmap:
#                 return True
#             hashmap[num]=1
#         return False