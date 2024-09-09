class Solution(object):
    def getSum(self, a, b):
        bitShortner = 0xffffffff
        while ((bitShortner &b)>0):
            temp = int( (a&b) << 1)
            a= a ^ b
            b=temp
        return (a & bitShortner) if b>0 else a
        