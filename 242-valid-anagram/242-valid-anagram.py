class Solution(object):
    def isAnagram(self, s, t):
        s=sorted(s)
        t=sorted(t)
        if s==t:
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
            
        