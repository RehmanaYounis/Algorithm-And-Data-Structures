class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        nums=s
        hashmap={}
        l=0
        res = 0
        curMax=0
        curLen = 0
        for r in range (len(s)):
            hashmap[s[r]]=1+hashmap.get(s[r],0)
            curMax=max(hashmap.values())
            curLen= r-l+1
            while (r - l + 1)-max(hashmap.values()) > k:
                hashmap[s[l]]-=1
                l+=1     
            res=max(res, r-l + 1)
            # r+=1
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ashmap=dict()
#         count = 0
#         l,r=0,0
#         maxLen=0
#         subLen=0
#         for i in s:
            
            
#             hashmap[i] = 1+ hashmap.get(i,0)
            
#             subLen= r-l+1
#             while subLen - max(hashmap.values()) > k:
#                 hashmap[s[l]]= hashmap[s[l]]-1
#                 print('see',hashmap[s[l]])
#                 l=l+1
#                 print(hashmap)
                
            
            
#             maxLen= max(maxLen, subLen)
#             r=r+1
            
#         return(maxLen-1)
        
        