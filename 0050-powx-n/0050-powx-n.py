class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res=helper(x,n//2 )
            res=res*res
            if n%2 == 0:
                return res
            else:
                return x* res
        
        res=helper(x, abs(n))
        if n>=0:
            return res
        else:
            return (1/res)
            
        
        
        
        
        
        
        # res=1
        # if n>0:
        #     for i in range(n):
        #         res*=x
        # else:
        #     n=abs(n)
        #     for i in range(n):
        #         res*=(1/x)
        #         print(res)
        # return res