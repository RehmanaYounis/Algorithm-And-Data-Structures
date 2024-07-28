class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap ={}
        tmap={}
        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            smap[s[i]]=1+smap.get(s[i], 0)
            tmap[t[i]]=1+tmap.get(t[i], 0)
        return smap == tmap
            
        
            