class Solution(object):
    def groupAnagrams(self, strs):
        ana_map=defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')]+=1
            ana_map[tuple(count)].append(s)
        return ana_map.values()