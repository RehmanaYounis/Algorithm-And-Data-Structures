class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i,val in enumerate(nums):
            num=abs(val)
            if nums[num-1] < 0:
                res.append(num)
            nums[num-1]*=-1
        return res
           
    
