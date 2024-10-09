class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        for i in reversed(range(len(nums1))):
            if n-1>=0 and nums2[n-1]>=nums1[m-1] or (m-1)<0:
                nums1[i]=nums2[n-1]
                n-=1
            else:
                nums1[i]=nums1[m-1]
                m-=1
            