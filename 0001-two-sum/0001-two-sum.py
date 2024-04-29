class Solution(object):
    def twoSum(self, nums, target):
        sumSet={}
        for index, num in enumerate(nums):
            if num in sumSet:
                return [sumSet[num], index]
            else:
                sumSet[target-num]=index
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         sMap=defaultdict(int)
#         for index,i in enumerate((nums)):
#             if i not in sMap:
#                 sMap[target-i] = index
#             else:
#                 return [sMap[i], index]
        