class Solution(object):
    def rob(self, nums):
        
        def MainRob(nums):
            hashMap={}
            if len(nums)==1:
                return nums[0]
            
            def dfs(n):
                if n > len(nums)-1:
                    return 0
                if n in hashMap:
                    return hashMap[n]
                choice1=nums[n]+dfs(n+2)
                choice2=dfs(n+1)
                hashMap[n]= max(choice1, choice2)
                return  hashMap[n]
            return dfs(0)
        
        
        if len(nums)==0: return 0
        if len(nums)==1: return nums[0]
        return max(MainRob(nums[1:]), MainRob(nums[:-1]))
        
        