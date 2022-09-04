class Solution(object):
    def characterReplacement(self, s, k):
        smap=defaultdict(int)
        maxLen=0
        l=0
        r=0
        while r<len(s):
            smap[s[r]] = 1+ smap.get(s[r],0)    
            curLen= r-l+1
            if curLen-max(smap.values())>k:
                smap[s[l]]-=1
                l+=1           
            maxLen=max(maxLen, r-l+1)
            r+=1
        return maxLen
        
#         sMap[s[r]] = 1+ sMap.get(s[r],0)           
#             curLen=r-l+1          
#             if curLen - max(sMap.values()) >k:
#                 sMap[s[l]]-=1
#                 l+=1
#             maxLen=max(maxLen, r-l+1)
#             r+=1
#         return maxLen
    