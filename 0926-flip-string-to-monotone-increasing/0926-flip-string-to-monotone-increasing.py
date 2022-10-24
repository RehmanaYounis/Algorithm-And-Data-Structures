class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        oneCount=0
        potentFlip=0
        i=0
        while s[i] != '1':
            i+=1
        for i in range(i, len(s)):
            if s[i]=='1':
                oneCount+=1
            elif s[i]=='0':
                potentFlip+=1
            if potentFlip>oneCount:
                potentFlip=oneCount
        return potentFlip