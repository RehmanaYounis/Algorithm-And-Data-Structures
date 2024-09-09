class Solution(object):
    def countBits(self, n):
#         dp=[0]* (n+1)
#         offset=1
#         for i in range(1, n+1):
#             if offset *2 ==i:
#                 offset=i
                
#             dp[i]=1 +dp[i-offset]
#         return dp

        def countBits(n):
            count=0
            while n:
                if n&1==1:
                    count+=1
                n=n>>1
            return count
        res=[]
        for i in range(n+1):
            res.append(countBits(i))
        return res