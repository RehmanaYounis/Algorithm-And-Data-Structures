class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(32):
            rev = rev << 1
            bit=n&1 
            rev = rev | bit
            n=n>>1
        return rev