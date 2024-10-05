class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # org = [1,2,3,4]
        # pre = [1,1,2,6]
        # post= [24,12,4,1]
        #prod= [24,12,8,6]
        
        pre=[1]*len(nums)
        post=[1]*len(nums)
        
        preV=1
        for i in range(1, len(nums)):
            pre[i]= preV * nums[i-1]
            preV=pre[i]
        postV=1    
        for i in reversed(range(len(nums)-1)):
            post[i]=postV * nums[i+1]
            postV=post[i]
        
        for i in range(len(pre)):
            pre[i]=pre[i]*post[i]
        return pre
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         pref=[1]*len(nums)
#         post=[1]*len(nums)
        
#         for i in range(1, len(nums)):
#             pref[i]=pref[i-1]*nums[i-1]
            
#         for i in reversed(range(len(nums)-1)):
#             post[i]=post[i+1]*nums[i+1]
    
        
#         for i in range(len(nums)):
#             pref[i]=pref[i]*post[i]
#         return pref
        