from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s=Counter(s)
        t=Counter(t)
        count=0
        for i in s.keys():
            # print(s[i], t[i])
            count+=max(0,(s[i]-t[i]))
        return count
            
        
        