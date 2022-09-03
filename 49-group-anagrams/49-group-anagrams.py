class Solution(object):
    def groupAnagrams(self, strs):
        aMap=defaultdict(list)
        for word in strs: 
            k=''.join(sorted(word))
            aMap[k].append(word)

        
        return aMap.values()
        