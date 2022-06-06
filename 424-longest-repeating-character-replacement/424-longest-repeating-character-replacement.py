class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap=defaultdict()
        l=0;
        maxLen=0; curLen=0;
        for r in range(len(s)):
            curLen=r-l+1
            hashmap[s[r]]=1 + hashmap.get(s[r],0 )
            while (curLen- max(hashmap.values()) > k):
                hashmap[s[l]]-=1
                l+=1
                curLen=r-l+1
                
            
            maxLen=max(maxLen, curLen)
        return(maxLen)