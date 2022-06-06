class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap=defaultdict();
        l=0; maxLen=0
        for r in range(len(s)):
            # print(s[r],'  ' ,hashmap)
            if s[r] in hashmap:
                while s[r] in hashmap:
                    hashmap.pop(s[l])
                    l+=1
            curLen=(r-l+1)
            maxLen=max(maxLen, curLen)
            hashmap[s[r]]=r
        return maxLen
        