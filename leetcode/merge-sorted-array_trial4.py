class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        first, sec = m - 1, n-1
        index = m + n - 1

        while sec >= 0:
            if first >= 0 and nums2[sec] < nums1[first]:
                nums1[index] = nums1[first]
                first -= 1
            else:
                nums1[index] = nums2[sec]
                sec -= 1
            index -= 1
        return nums1

