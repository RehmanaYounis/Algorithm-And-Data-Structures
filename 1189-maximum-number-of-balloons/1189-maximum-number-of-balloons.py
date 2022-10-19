class Solution(object):
    def maxNumberOfBalloons(self, text):
        hashMap=defaultdict(int)
        for i in text:
            hashMap[i]+=1
        
        b=hashMap['b']
        count=0
        
        while b:
            if hashMap['a'] >=1 and hashMap['l']>=2 and hashMap['o']>=2 and hashMap['n']>=1:
                hashMap['a']-=1
                hashMap['l']-=2 
                hashMap['o']-=2
                hashMap['n']-=1
                b-=1
                count+=1
            else:
                return count
            
        return count
            
            
            
        