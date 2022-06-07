class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2): return False
        l = 0
        r = len(s1)
        s1Count = collections.Counter(s1)
        while r <= len(s2):
            if s1Count == collections.Counter(s2[l:r]):
                return True  
            l += 1
            r += 1
            
        return False
    
    
#         if len(s1)>len(s2): return False
#         s1Map=collections.Counter(s1)
#         l=0; r=len(s1)
#         while r<=len(s2):
#             if s1Map==collections.Counter(s2[l:r]):
#                 return True
#             l+=1
#             r+=1
#         return False
        
        
        
                
#         l = 0
#         r = len(s1)
#         s1Count = collections.Counter(s1)
#         print(s1Count)
#         while r <= len(s2):
#             if s1Count == collections.Counter(s2[l:r]):
#                 return True  
#             l += 1
#             r += 1
            
#         return False