class Solution(object):
    def isPalindrome(self, s):
        print(len(s))
        s=s.lower()
        def isAlphaNum(c):
            if (ord("A")<= ord(c) <= ord("Z") or
                ord("a")<= ord(c) <= ord("z") or
                ord("0")<= ord(c) <= ord("9")               
               ):
                return True
            else:
                return False
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not isAlphaNum(s[l]):
                    l+=1
            while l<r and not isAlphaNum(s[r]):
                    r-=1
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
                    
            
        