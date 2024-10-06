class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) ==0: return True
        if len(s) > len(t): return False
        l=0
        for ind,val in enumerate(t):
            if l<len(s) and s[l] == val:
                print(s[l],l)
                l+=1
                
        if l>=len(s):
                return True     
        return False