class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        minLen=len(s1)
        l=0
        r=0
        if len(s1)>len(s2):
            return False
        while r<len(s2)-minLen+1:
            curStr=s2[r:r+minLen]
            if Counter(s1)==Counter(curStr):
                return True
            r+=1
        return False