# Brute Force
class Solution:
    def trap(self, height: List[int]) -> int:
        rMax = [0] * len(height)
        rMax[len(height)-1] = height[len(height)-1]
        lMax = height[0]
        res = 0

        for i in range(len(height)-2, 0, -1):
            rMax[i] = max(height[i], rMax[i+1])
        
        for i in range(1, len(height)-1):
            if height[i] < lMax and height[i] < rMax[i]:
                res += min(lMax, rMax[i]) - height[i]
            
            lMax = max(lMax, height[i])
        
        return res

# Optimized
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        lMax, rMax = height[0], height[len(height)-1]
        res = 0

        while left < right:
            if lMax < rMax:
                left += 1
                res += max(0,lMax - height[left])
                lMax = max(lMax, height[left])
            else:
                right -= 1
                res += max(0,rMax - height[right])
                rMax = max(rMax, height[right])
        return res