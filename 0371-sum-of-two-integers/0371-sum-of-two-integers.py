#https://www.youtube.com/watch?v=_pUidg9gQyA
class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitShort=0xffffffff
        while (bitShort&b) > 0:
            carry = (a&b)<<1
            a = a^b
            b=carry
        return (a & bitShort) if b>0 else a
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
#         bitShortner=0xffffffff
#         while ((b&bitShortner)>0):
#             carry=int((a & b)<<1)
#             a=a^b
#             b=carry
#         return (a & bitShortner) if b>0 else a
        
        