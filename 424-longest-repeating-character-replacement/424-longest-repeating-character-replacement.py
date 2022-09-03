class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sMap={}
        l,r=0,0
        maxLen=0
        while r<len(s):
            sMap[s[r]] = 1+ sMap.get(s[r],0)           
            curLen=r-l+1          
            if curLen - max(sMap.values()) >k:
                sMap[s[l]]-=1
                l+=1
            maxLen=max(maxLen, r-l+1)
            r+=1
        return maxLen
    
    
