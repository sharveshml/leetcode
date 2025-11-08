class Solution:
    def isPossible(self, pages: int, arr: list, k: int):
        count = 0
        sum = 0
        
        for i in arr:
            if sum + i > pages:
                count += 1
                sum = i
                
                if sum > pages:
                    return False
            else:
                sum += i
        
        return True if count < k else False
        
    def findPages(self, arr, k):
        if k > len(arr):
            return -1
            
        lo = min(arr)
        hi = sum(arr)
        pages = 0
        
        while lo < hi:
            
            mid = (lo + hi) // 2
            if self.isPossible(mid, arr, k):
                hi = mid
            else:
                lo = mid + 1
        
        return lo