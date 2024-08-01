class Solution(object):
    def groupAnagrams(self, strs):
        angMap=defaultdict(list)
        
        for words in strs:
            count=[0]*26
            for ch in words:
                count[ord(ch)-ord('a')]+=1
            angMap[tuple(count)].append(words)
        return angMap.values()