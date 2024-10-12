class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for r in reversed(range(len(nums1))):
            if (n-1 >=0 and nums2[n-1]>=nums1[m-1]) or m-1 <0:
                nums1[r]=nums2[n-1]
                n-=1
            elif m-1>=0:
                nums1[r]=nums1[m-1]
                m-=1
        