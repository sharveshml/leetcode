class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0

        # Find median.
        for count in range(0, (n + m) // 2 + 1):
            m2 = m1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < n:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1

        # Check if the sum of n and m is odd.
        if (n + m) % 2 == 1:
            return float(m1)
        else:
            ans = float(m1) + float(m2)
            return ans / 2.0

# Optimal Solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(nums1)-1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            l1 = nums1[i] if i >= 0 else float('-inf')
            r1 = nums1[i+1] if i+1 < len(nums1) else float('inf')
            l2 = nums2[j] if j >= 0 else float('-inf')
            r2 = nums2[j+1] if j+1 < len(nums2) else float('inf')

            if l2 <= r1 and l1 <= r2:
                if total % 2:
                    return min(r1, r2)
                else:
                    return (max(l1,l2) + min(r1,r2))/2
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1

