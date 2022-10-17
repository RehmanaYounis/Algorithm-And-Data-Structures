class Solution(object):
    def longestCommonPrefix(self, strs):
        res=''
        for chIndex in range(len(strs[0])):
            for string in strs:
                if chIndex == len(string) or string[chIndex] != strs[0][chIndex]:
                    return res
            res+=strs[0][chIndex]
        return res
        