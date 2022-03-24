class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping={}
        map2={}
        if len(s) != len(t):
            return False
        
        def helper(s,t):
            
            for i in range(len(s)):
                c1 = s[i]
                c2=t[i]
                if c1 in mapping and mapping[c1] != c2 or (c2 in map2 and map2[c2] != c1):
                    return False        
            
                mapping[c1]=c2
                map2[c2]=c1
            return True
        
        return (helper(s,t))