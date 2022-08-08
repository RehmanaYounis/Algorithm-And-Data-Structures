class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen= len(nums1)+len(nums2)
        if len(nums1)<len(nums2):
            A=nums1
            B=nums2
        else: 
            A=nums2
            B=nums1
        print(A)
        half=totalLen//2
        l=0; r = len(A)-1
        while True:
            midA=(l+r)//2
            midB= half-midA -2
            
            leftA=A[midA] if midA>=0 else float('-infinity')
            rightA=A[midA+1] if (midA+1) < len(A) else float('infinity')
            leftB=B[midB]  if midB >=0 else float('-infinity')
            rightB=B[midB+1] if (midB+1) <len(B) else float('infinity')
            
            if leftA <= rightB and leftB <=rightA:
                print('ok', leftA, leftB, rightA, rightB)
                if (totalLen%2 == 0):
                    med = (max(leftA,leftB) + min(rightA,rightB))/2
                else:
                    med= min(rightA, rightB)
                return med
            elif leftA<rightB:
                l=midA+1
            else:
                r=midA-1
            