#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        half = (n + m) // 2
        lo, hi = 0, len(nums1)-1

        while True:
            mid1 = (lo + hi) // 2
            mid2 = half - mid1 - 2

            l1 = nums1[mid1] if mid1 >= 0 else float('-inf')
            r1 = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float('inf')
            l2 = nums2[mid2] if mid2 >=0 else float('-inf')
            r2 = nums2[mid2+1] if mid2+1 < len(nums2) else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (n+m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)
            
            elif l1 > r2:
                hi = mid1 - 1
            else:
                lo = mid1 + 1


# @lc code=end

