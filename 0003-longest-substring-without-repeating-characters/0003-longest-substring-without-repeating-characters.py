class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chrSet=set()
        maxLen=0
        l=0
        for r in range(len(s)):
            while s[r] in chrSet:
                chrSet.remove(s[l])
                l+=1
            maxLen=max(maxLen, (r-l+1))
            chrSet.add(s[r])
        return maxLen