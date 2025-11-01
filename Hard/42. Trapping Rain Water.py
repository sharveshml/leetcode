from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left, right = 0, n - 1
        lmax, rmax = 0, 0
        res = 0

        while left < right:
            # If the left wall is shorter or equal, the water level is limited by the left side.
            if height[left] <= height[right]:
                if height[left] >= lmax:
                    # This bar is a new high wall, it can't trap water. Update lmax.
                    lmax = height[left]
                else:
                    # This bar is shorter than lmax, so it traps water.
                    res += lmax - height[left]
                left += 1
            # If the right wall is shorter, the water level is limited by the right side.
            else:
                if height[right] >= rmax:
                    # This bar is a new high wall, it can't trap water. Update rmax.
                    rmax = height[right]
                else:
                    # This bar is shorter than rmax, so it traps water.
                    res += rmax - height[right]
                right -= 1
        
        return res
