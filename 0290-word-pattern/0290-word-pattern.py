class Solution(object):
    def wordPattern(self, pattern, s):
        cMap={}
        wMap={}
        words = s.split(' ')
        if len(pattern)!= len(words):
            return False
        for ch, word in zip(pattern, words):
            if ch in cMap and cMap[ch] != word:
                return False
            if word in wMap and wMap[word] != ch:
                return False
            cMap[ch]=word
            wMap[word]=ch
        return True