class Solution(object):
    def groupAnagrams(self, strs):
        hashmap={}
        for s in strs:
            # temp = "".join(sorted(s))
            temp=tuple(sorted(s))
            # print(temp)
            if temp not in hashmap:
                hashmap[temp]=[s]
            else:
                hashmap[temp]=hashmap[temp]+[s]
                
        return hashmap.values()
        
        
        
    