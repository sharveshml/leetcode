class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, lmax, right, rmax, res = 0, 0, n-1, height[n-1], 0

        while left < right:
            if height[left] < lmax and height[left] < rmax:
                res += min(lmax, rmax) - height[left]

                lmax = max(lmax, height[left])
            if height[right] < rmax and height[right] < lmax:
                res += min(lmax, rmax) - height[right]

                rmax = max(rmax, height[right])

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return res