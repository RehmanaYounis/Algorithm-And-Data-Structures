class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):return False
        if s =='': return True
        l=0
        for ind, ch in enumerate(t):
            if s[l]==ch:
                l+=1
                if l==len(s):
                    return True
        return False