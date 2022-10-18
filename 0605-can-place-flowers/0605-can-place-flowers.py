class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        temp=[0]+flowerbed+[0]
        for i in range(1,len(flowerbed)+1):
            if temp[i-1]==0 and temp[i]==0 and temp[i+1]==0:
                n-=1
                temp[i]=1
            if n<=0:
                    return True
        return False