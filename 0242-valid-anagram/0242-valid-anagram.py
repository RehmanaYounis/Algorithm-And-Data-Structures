class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        sMap=Counter(s)
        tMap=Counter(t)
        for key, val in sMap.items():
            if sMap[key] != tMap[key]:
                return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(s) != len(t): return False
#         sMap, tMap ={}, {}
#         for i in range(len(s)):
#             sMap[s[i]] =1 + sMap.get(s[i],0)
#             tMap[t[i]] =1 + tMap.get(t[i],0)
#         for key in sMap:
#             print(key, sMap[key],sMap[key])
#             if sMap[key] != tMap.get(key, 0):       
#                 return False
            
#         return True
            
# #             sMap[s[i]] =1 + sMap.get(s[i],0)
# #         print (sMap)
    
    
    
    
        # smap=Counter(s)
        # tmap=Counter(t)
        # if smap==tmap:
        #     return True
        # else:
        #     return False