class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rev=0
        for i in range(32):
            rev = rev <<1
            digit=n&1
            rev = rev|digit
            n=n>>1
        return rev
   