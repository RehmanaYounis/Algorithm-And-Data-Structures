class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for ind, num in enumerate(nums):
            if ind >0 and nums[ind -1]==num:
                continue
        
            l=ind+1
            r=len(nums)-1
            
            while l<r:
                curSum = num + nums[l]+nums[r]
                if curSum <0:
                    l+=1
                elif curSum>0:
                    r -=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res