class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(' ')
        print(len(s))
        if len(pattern) != len(s):
            return False
        
        pmap = {}
        wmap={}
        
        for i in range(len(pattern)):
            c= pattern[i]
            word1=s[i]
            if c  in pmap and pmap[c]!= word1 or ( word1  in wmap and wmap[word1]!= c):
                return False
            pmap[c]=word1
            wmap[word1]=c
        return True