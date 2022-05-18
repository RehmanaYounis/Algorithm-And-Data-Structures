class Solution(object):
    def productExceptSelf(self, nums):
        prefix= [1]* len(nums)
        sufix= [1]* len(nums)
        for i in range(1, len(nums)): 
            prefix[i]=prefix[i-1]*nums[i-1]
             
        for i in range(len(nums)-1, 0, -1):
            sufix[i-1]=sufix[i]*nums[i]
            
        for i in range(len(nums)):
            prefix[i]=prefix[i]*sufix[i]
        return (prefix)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         forward=[1]*len(nums)
#         backward = [1]* len(nums)
        
#         prod = 1
        
#         for i in range (len(nums)):
#             forward[i]=prod
#             prod = prod * nums[i]
            
#         prod = 1
        
#         for i in reversed(range(len(nums))):
#             backward[i]= prod
#             prod = prod * nums[i]
            
#         for i in range (len(nums)):
#             nums[i]= forward[i] * backward[i]
            
#         return nums
            
            
        
                         
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         forward= [1]*len(nums)
#         backward= [1]*len(nums)
        
#         prod=1
#         for i in range(len(nums)):
#             forward[i] = prod
#             prod= prod * nums[i]
        
#         prod= 1
        
#         for i in reversed(range(len(nums))):
#             backward[i]= prod
#             prod = prod * nums[i]
        
#         print (forward)
#         for i in range (len(nums)):
#             forward[i]=forward[i] *backward[i]
#         return forward
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         prefix= [(1)] * len(nums)
#         prod = 1
#         for i in range(1,len(nums)):
#             prod = prod*nums[i-1]
#             prefix[i]=prod
#         print(prefix)
#         prod=1
#         postfix=[(1)] * len(nums)
#         for i in reversed( range( len(nums))):
#             prefix[i]=prod *prefix[i]
#             prod=prod*nums[i]
#         return prefix
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         result = [1]*  len(nums)
#         prod = 1
#         for i in range(1, len(nums)):
#             prod = prod * nums[i-1]
#             result[i]=prod
        
#         prod = 1
#         for i in  reversed(range(len(nums) - 1)):
#             print (i)
#             prod = prod * nums[i+1]
#             result[i] = prod * result[i]
#         return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        