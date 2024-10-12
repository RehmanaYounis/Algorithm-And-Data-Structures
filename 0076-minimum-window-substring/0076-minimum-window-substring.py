class Solution(object):
    def minWindow(self, s, t):
        tmap=Counter(t)
        need = len(tmap)
        have=0
        smap=defaultdict(int)
        minLen=float('inf')
        res=''
        l=0
        for ind,ch in enumerate(s):
            smap[ch]+=1
            if ch in tmap and smap[ch]==tmap[ch]:
                have+=1
            while need == have:
                curLen=(ind-l+1)
                if curLen< minLen:
                    minLen=curLen
                    res=s[l:ind+1]
                if s[l] in tmap:
                    smap[s[l]]-=1
                if smap[s[l]] < tmap[s[l]]:
                    have-=1
                l+=1
                    
        return res
            
        