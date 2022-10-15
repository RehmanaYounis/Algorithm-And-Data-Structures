class Solution(object):
    def longestPalindrome(self, s):
        maxStr=''
        maxLen=0
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r <len(s) and s[l]==s[r]:
                if (r-l+1)>maxLen:
                    maxLen=r-l+1
                    maxStr=s[l:r+1]
                l-=1
                r+=1
        for i in range(len(s)):
            l=i
            r=i+1
            while l>=0 and r <len(s) and s[l]==s[r]:
                if (r-l+1)>maxLen:
                    maxLen=r-l+1
                    maxStr=s[l:r+1]
                l-=1
                r+=1
        return maxStr
        