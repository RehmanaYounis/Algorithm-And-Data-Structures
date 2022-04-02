class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s=Counter(s)
        t=Counter(t)
        count=0
        for i in s.keys():
            if s[i]>t[i]:
                count+=s[i]-t[i] 
        for i in t.keys():
            if t[i]>s[i]:
                count+=t[i]-s[i] 
        return count