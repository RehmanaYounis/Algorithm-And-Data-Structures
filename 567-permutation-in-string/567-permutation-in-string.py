class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        s1Count = collections.Counter(s1)
        
        while r <= len(s2):
            if s1Count == collections.Counter(s2[l:r]):
                return True  
            l += 1
            r += 1
            
        return False