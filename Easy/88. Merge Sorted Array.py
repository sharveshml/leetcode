class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        ptr1 = m-1
        ptr2 = n-1
        total_length = m+n-1

        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[total_length] = nums1[ptr1]
                total_length -= 1
                ptr1 -= 1
            else:
                nums1[total_length] = nums2[ptr2]
                total_length -= 1
                ptr2 -= 1

        while ptr2 >= 0:
            nums1[total_length] = nums2[ptr2]
            total_length -= 1
            ptr2 -= 1