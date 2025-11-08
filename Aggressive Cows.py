class Solution:
    def _place (self, stalls:list, ind: int, placed: list, k: int):
        if len(placed) == k:
            min_dist = min(
                    placed[i+1] - placed[i] for i in range(len(placed) - 1)
                )
            
            self.max_dist = max(self.max_dist, min_dist)
            return
        
        if ind == len(stalls):
            return
        
        self._place(stalls, ind+1, placed+[stalls[ind]], k)
        self._place(stalls, ind+1, placed, k)
        
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        self.max_dist = 0
        self._place(stalls, 0, [], k)
        
        return self.max_dist


class Solution:
    def isPossible(self, dist: int, stalls: list, k: int) -> bool:
        count = 1
        prev = stalls[0]
        
        for i in range(1, len(stalls)):
            if stalls[i] - prev >= dist:
                count += 1
                prev = stalls[i]
        
        return count >= k
                
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        lo = 1
        hi = stalls[-1] - stalls[0] + 1
        res = 0
        
        while lo < hi:
            
            mid = (lo + hi) // 2
            
            if self.isPossible(mid, stalls, k):
                res = mid
                lo = mid + 1
            else:
                hi = mid
            
        return res
    
    
a = Solution()
print(a.aggressiveCows([1, 2, 4, 8, 9], 3))