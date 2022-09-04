class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strSet=set()
        l=0
        r=0
        maxLen=0
        while r<len(s):
            
            
            while s[r] in strSet:
                strSet.remove(s[l])
                l+=1
            strSet.add(s[r])
            maxLen=max(maxLen,r-l+1)
            r+=1
        return maxLen
        
