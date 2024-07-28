class Solution(object):
    def isPalindrome(self, s):
        def isAlphnum(c):
            if ('A'<= c <= 'Z' or
               'a'<= c <= 'z' or
                '0'<= c <= '9'):
                return True
            else:
                return False
        s=s.lower()
        l=0
        r=len(s) -1
        while l<r:
            while l<r and not isAlphnum(s[l]):
                l+=1
            while l<r and not isAlphnum(s[r]):
                r-=1
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
                    
            
            
        