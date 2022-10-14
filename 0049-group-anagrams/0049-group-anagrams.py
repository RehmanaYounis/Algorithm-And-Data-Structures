class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)
        for cur in strs:
            key=''.join(sorted(cur))
            if key in hashMap:
                hashMap[key].append(cur)
            else:
                hashMap[key]=[cur]
        res=[]
        for key in hashMap:
            res.append(hashMap[key])
        return res