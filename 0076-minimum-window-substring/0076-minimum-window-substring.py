class Solution(object):
    def minWindow(self, s, t):
        if len(t) =="": return ""
        sMap,tMap = defaultdict(int), Counter(t)
        required= len(tMap)
        matched=0
        res=''
        resLen=float('inf')
        l=0
        for r in range(len(s)):
            rval=s[r]
            sMap[rval]+=1
            if rval in tMap and sMap[rval]==tMap[rval]:
                matched+=1
            while required == matched:
                if (r-l+1) < resLen:
                    resLen=r-l+1
                    res=s[l:r+1]
                lval=s[l]
                if lval in tMap:
                    sMap[lval]-=1
                    if sMap[lval] < tMap[lval]:
                        matched-=1
                l+=1
        return res
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         tmap=Counter(t)
#         smap= {s:0 for s in tmap.keys()}
#         need=len(tmap)
#         having = 0
        
#         l=0
#         r=0
#         minLen=float('inf')
#         res=''
        
#         while r< len(s):
#             cur=s[r]
#             if cur in smap:
#                 smap[cur]+=1
#                 if smap[cur] == tmap[cur]:
#                     having+=1
#             while having==need:
#                 curLen = r-l+1
#                 if curLen<minLen:
#                     minLen=curLen
#                     res=s[l:r+1]
#                 if s[l] in smap:
#                     smap[s[l]]-=1
#                     if smap[s[l]] < tmap[s[l]]:
#                         having-=1
#                 l+=1
                
#             r+=1
#         return res
            
        