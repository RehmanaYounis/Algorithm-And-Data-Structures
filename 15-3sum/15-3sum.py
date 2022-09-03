class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res=[]
        for ind, num in enumerate(nums):
            if ind > 0 and num == nums[ind - 1]:
                continue
            l=ind+1
            r=len(nums)-1
            while l<r:
                curSum = num+nums[l]+nums[r]
                if curSum <0:
                    l+=1
                elif curSum>0:
                    r-=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                
        return res
        