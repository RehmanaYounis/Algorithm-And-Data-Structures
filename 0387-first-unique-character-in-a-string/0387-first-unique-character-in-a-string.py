class Solution:
    def firstUniqChar(self, s: str) -> int:
        cmap=Counter(s)
        for ind,ch in enumerate(s):
            if cmap[ch]==1:
                return ind
        return -1