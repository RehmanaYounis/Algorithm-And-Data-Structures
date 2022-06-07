class Solution(object):
    def minWindow(self, s, t):
        tmap=collections.Counter(t)
        smap = collections.defaultdict(int)
        if len(t) > len(s): return ""
        l, r =0,0
        output=''
        minLen = float('inf')
        need=len(tmap.keys())
        having = 0
        for r in range(len(s)):
            
            smap[s[r]]+=1;
            if smap[s[r]] == tmap[s[r]]:
                having+=1
            while having == need :
                if( r-l+1)< minLen:
                    minLen=r-l+1
                    output=s[l:r+1]
                smap[s[l]]-=1
                # print(s, l)
                if s[l] in tmap and smap[s[l]]<tmap[s[l]]:
                    having-=1
                l+=1
        return (output)
        