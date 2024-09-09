#https://www.youtube.com/watch?v=_pUidg9gQyA
class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitShortner=0xffffffff
        while ((b&bitShortner)>0):
            carry=int((a & b)<<1)
            a=a^b
            b=carry
        return (a & bitShortner) if b>0 else a
        
        
        # def getSum(self, a, b):
        # bitShortner = 0xffffffff
        # while ((bitShortner &b)>0):
        #     temp = int( (a&b) << 1)
        #     a= a ^ b
        #     b=temp
        # return (a & bitShortner) if b>0 else a
        