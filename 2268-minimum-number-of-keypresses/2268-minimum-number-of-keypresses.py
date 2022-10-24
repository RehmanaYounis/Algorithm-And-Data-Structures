class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count=0
        block=0
        nums=0
        keyMap=Counter(s)
        values=sorted(list(keyMap.values()))[::-1]
        for val in values:
            if nums<9:
                count+=val
            elif nums<18:
                count+=2*val
            elif nums<27:
                count+=3*val
            nums+=1
        return count