class Solution:
    def kthElement(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        lo, hi = max(0, k-m), min(k, n)

        while True:
            mid1 = (lo + hi) // 2
            mid2 = k - mid1

            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
            l2 = nums2[mid2-1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            
            elif l1 > r2:
                hi = mid1 - 1
            else:
                lo = mid1 + 1


# @lc code=end


        