class Solution(object):
    def minFlipsMonoIncr(self, s):
        oneCount=0
        posblFlip=0
        i=0
        while s[i] !='1':
            i+=1
        for ind in range(i, len(s)):
            if s[ind]=='1':
                oneCount+=1
            else:
                posblFlip+=1
            if posblFlip>oneCount:
                posblFlip=oneCount
        return posblFlip
        