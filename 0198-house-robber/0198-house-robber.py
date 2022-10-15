class Solution(object):
    
    def rob(self, nums):
        hashMap={}
        def dfs(n):
            if n>=len(nums):
                return 0
            if n in hashMap:
                return hashMap[n]
            choice1=nums[n]+dfs(n+2)
            choice2=dfs(n+1)
            hashMap[n]= max(choice1, choice2)
            return hashMap[n]
        
        maxCost=float('-inf')
        for i in range(len(nums)):
            maxCost=max(maxCost, dfs(i))
        return maxCost