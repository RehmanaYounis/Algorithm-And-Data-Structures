class Solution(object):
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        
        for i in range(len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                continue
            curVal=nums[i]
            left= i+1
            right= len(nums)-1
            while left<right:
                curSum=curVal+nums[left]+nums[right]
                if (curSum) ==0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    
                elif curSum>0:
                    right-=1
                else:
                    left+=1
            
        return triplets
