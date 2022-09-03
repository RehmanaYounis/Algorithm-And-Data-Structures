class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
    
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res
    
        cSet=set()
        maxLen=0
        l=0
        r=0
        
        for r in range(len(s)):# r<len(s)-1:
            
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1 
            cSet.add(s[r])
            maxLen=max(maxLen, r-l+1)
            # r+=1
        return maxLen