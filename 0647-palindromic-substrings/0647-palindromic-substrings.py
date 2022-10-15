class Solution(object):
    def countSubstrings(self, s):
        maxCount=0
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r <len(s) and s[l]==s[r]:
                maxCount+=1
                l-=1
                r+=1
        for i in range(len(s)):
            l=i
            r=i+1
            while l>=0 and r <len(s) and s[l]==s[r]:
                maxCount+=1
                l-=1
                r+=1
        return maxCount
        
        