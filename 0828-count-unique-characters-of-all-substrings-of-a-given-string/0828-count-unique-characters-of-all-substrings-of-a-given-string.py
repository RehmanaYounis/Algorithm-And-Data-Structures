class Solution(object):
    def uniqueLetterString(self, s):
        hashMap=defaultdict(list)
        
        for ind,c in enumerate(s):
            hashMap[c].append(ind)
        
        count=0
        for key in hashMap:
            cur=hashMap[key]
            cur=[-1]+cur+[len(s)]
            for j in range(1, len(cur)-1):         
                count+= (cur[j]-cur[j-1]) * (cur[j+1]-cur[j])                             
        return count   
      
        
        
        
        
        
     