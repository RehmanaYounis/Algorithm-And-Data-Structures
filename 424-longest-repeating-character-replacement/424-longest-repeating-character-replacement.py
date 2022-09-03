class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sMap={}
        l,r=0,0
        maxLen=0
        maxf=0
        while r<len(s):
            sMap[s[r]] = 1+ sMap.get(s[r],0)
            maxf = max(maxf, sMap[s[r]])
            curLen=r-l+1
            
            if curLen - max(sMap.values()) >k:
                sMap[s[l]]-=1
                l+=1
            maxLen=max(maxLen, r-l+1)
            r+=1

        return maxLen
    
    
    
#         count = {}
#         res = 0

#         l = 0
#         maxf = 0
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
#             maxf = max(maxf, count[s[r]])

#             if (r - l + 1) - maxf > k:
#                 count[s[l]] -= 1
#                 l += 1

#             res = max(res, r - l + 1)
#         return res

































    
    
    
    
    
     # sMap=defaultdict(int)
     #    l,r=0,0
     #    maxLen=0
     #    maxf=0
     #    while r<len(s):
     #        sMap[s[r]]+=1
     #        curLen=r-l+1
     #        temp = max(maxf, sMap[s[r]])
     #        while (curLen - temp ) >k:
     #            sMap[s[l]]-=1
     #            l+=1
     #        maxLen=max(maxLen, r-l+1)
     #        r+=1
     #    return maxLen