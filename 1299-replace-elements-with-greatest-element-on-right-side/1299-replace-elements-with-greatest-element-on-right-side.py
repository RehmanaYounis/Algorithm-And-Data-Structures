class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right=len(arr)-1
     
        while right>=0:
            print(arr[right])
            if (right+1)<len(arr):
                arr[right]=max(arr[right], arr[right+1])
            right-=1
            
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[-1]=-1
        return (arr)