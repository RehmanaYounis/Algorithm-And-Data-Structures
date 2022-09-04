class Solution(object):
    def minWindow(self, s, t):
        tmap=Counter(t)
        smap= {s:0 for s in tmap.keys()}
        need=len(tmap)
        having = 0
        
        l=0
        r=0
        minLen=float('inf')
        res=''
        
        while r< len(s):
            cur=s[r]
            if cur in smap:
                smap[cur]+=1
                if smap[cur] == tmap[cur]:
                    having+=1
            while having==need:
                curLen = r-l+1
                if curLen<minLen:
                    minLen=curLen
                    res=s[l:r+1]
                if s[l] in smap:
                    smap[s[l]]-=1
                    if smap[s[l]] < tmap[s[l]]:
                        having-=1
                l+=1
                
            r+=1
        return res
            
        