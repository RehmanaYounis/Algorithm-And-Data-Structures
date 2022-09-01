class Solution:
    def __init__(self):
            self.resLen =0
    def countSubstrings(self, s: str) -> int:
        
           

        def isPalindrome(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                self.resLen+=1
                l-=1
                r+=1

        for i in range(len(s)):
            l,r=i,i
            isPalindrome(l,r)
        for i in range(len(s)):
            l,r=i,i+1
            isPalindrome(l,r)
        print(self.resLen)
        return self.resLen