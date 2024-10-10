#[1,2,3,4]
#[1,1,2,6]
#[24,12,4,1]
#[24,12,8,6]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        post=[1]*len(nums)
        
        prev=1
        for i in range(1, len(nums)):
            pre[i]=nums[i-1]*prev
            prev=pre[i]
        
        pos=1
        for i in reversed(range(len(nums)-1)):
            post[i]=nums[i+1]*pos
            pos=post[i]
        
        for i in range(len(nums)):
            pre[i]=pre[i]*post[i]
        return pre
            