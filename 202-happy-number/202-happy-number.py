class Solution(object):
    def isHappy(self, n):
        def sumSq(num):
            curSum=0
            while num:
                digit=num%10
                num=num//10
                curSum+=(digit*digit)
            return curSum
        
        s1, s2=n, n
        while True:
            s1= sumSq(s1)
            s2= sumSq(sumSq(s2))
            if s1 ==s2:
                return s1 == 1


  

