class Solution:
    def uniqueLetterString(self, s: str) -> int:
        charMap=defaultdict(list)
        for idx, val in enumerate(s):
            charMap[val].append(idx)
        n=len(s)
        count=0
        for key, val in charMap.items():
            cur=[-1]+val+[n]
            for j in range(1, len(cur)-1):
                count+= ((cur[j]-cur[j-1])*(cur[j+1]-cur[j]))
        return(count)