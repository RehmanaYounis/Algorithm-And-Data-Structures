class Solution(object):
    def merge(self, nums1, m, nums2, n):
        first = m - 1
        sec = n - 1
        for i in reversed(range(len(nums1))):
            if sec >= 0 and (first < 0 or nums2[sec] >= nums1[first]):
                nums1[i] = nums2[sec]
                sec -= 1
            elif first >= 0:
                nums1[i] = nums1[first]
                first -= 1
        return nums1
