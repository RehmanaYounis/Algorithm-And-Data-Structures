class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(i,target):
            if (i,target) in dp:
                return dp[(i,target)]
            if i==len(nums) and target==0:
                return 1
            if i>=len(nums):
                return 0
            case1=dfs(i+1, target+nums[i] )
            case2=dfs(i+1,  target-nums[i])
            dp[(i,target)]=case1+case2
            return dp[(i,target)]
        return dfs(0, target)