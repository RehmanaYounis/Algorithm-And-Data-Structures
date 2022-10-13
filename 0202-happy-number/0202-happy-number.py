class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n==4:
            return False
        sumV=0
        while n:
            digit=n%10
            n=n//10
            sumV+=digit*digit
        if self.isHappy(sumV): return True
            
            