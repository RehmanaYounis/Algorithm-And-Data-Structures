class Solution(object):
    def firstUniqChar(self, s):
        charSet=defaultdict(int)
        for i in s:
            charSet[i]+=1
        for idx,val in enumerate(s):
            if charSet[val]==1:
                return idx
        return -1
            