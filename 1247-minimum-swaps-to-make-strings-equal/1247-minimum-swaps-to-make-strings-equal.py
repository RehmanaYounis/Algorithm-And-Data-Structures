class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cx,cy=0,0
        if len(s1)!= len(s2):
            return -1
        
        for i in range(len(s1)):
            print(s1[i], s2[i])
            if s1[i]=='x' and s2[i]=='y':
                cx+=1
            elif s1[i]=='y' and s2[i]=='x':
                cy+=1
        if cx  % 2==0 and cy%2 ==0:
            return cx//2 +cy//2
        if (cx+cy)%2 ==0:
            return (cx//2 +cy//2)+2
        return -1