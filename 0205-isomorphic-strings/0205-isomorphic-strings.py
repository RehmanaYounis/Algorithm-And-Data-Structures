class Solution(object):
    def isIsomorphic(self, s, t):
        hashMap={}
        for i in range(len(s)):
            if s[i] not in hashMap and t[i] not in hashMap.values():
                hashMap[s[i]]= t[i]
        
        res=''
        for i in range(len(s)):
            if s[i] not in hashMap: return False
            res+=hashMap[s[i]]
        return res==t
                
        