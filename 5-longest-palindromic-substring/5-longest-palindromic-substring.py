class Solution:
    def __init__(self):
        self.res=""
    def longestPalindrome(self, s: str) -> str:
        # res=[]
        resLen=[0]
        
        def isPalindrome(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen[0]:
                    resLen[0] = (r-l+1)
                    self.res=s[l:r+1]
                l-=1
                r+=1
        
        for i in range(len(s)):
            l,r=i,i
            isPalindrome(l,r)
        for i in range(len(s)):
            l,r=i,i+1
            isPalindrome(l,r)
        return self.res
            