from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        smap=defaultdict()
        tmap=defaultdict()
        for i in s:
            if i not in smap:
                smap[i]=0
            else:
                smap[i]=smap[i]+1
        for i in t:
            if i not in tmap:
                tmap[i]=0
            else:
                tmap[i]=tmap[i]+1
        if smap==tmap:
            return True
        else:
            return False
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(s) != len(t):
#             return False
#         smap , tmap = {}, dict()
#         for i in range(len(s)):
#             smap[s[i]]= 1+ smap.get(s[i], 0)
#             tmap[t[i]]= 1+ tmap.get(t[i], 0)
#         for i in smap.keys():
#             if i not in tmap or smap[i] != tmap[i]:
#                 return False
#         return True
            
        