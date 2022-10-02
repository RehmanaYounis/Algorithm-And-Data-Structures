class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[]
        count=Counter(nums)
        def dfs():
            if len(stack)==len(nums):
                res.append(stack[::])
                return
           
            for key in count:
                if count[key]>0:
                    stack.append(key)
                    count[key]-=1
                    dfs()
                    stack.pop()
                    count[key]+=1
                
        dfs()
        return res