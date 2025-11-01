# TLE
class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        
        timings = []
        for i in range(len(arr)):
            timings.append([arr[i],dep[i]])
        
        timings.sort(key=lambda x:x[0])
        
        platforms = 1
        max_platforms = 1
        ongoing = [timings[0][1]]
        
        for i in range(1, len(timings)):
            arrival, departure = timings[i][0],  timings[i][1]
            
            ongoing = [d for d in ongoing if d >= arrival]
            
            ongoing.append(departure)
            
            platforms = len(ongoing)
            max_platforms = max(platforms, max_platforms)
        
        return max_platforms
        
        
# Optimized
class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        
        arr.sort()
        dep.sort()
       
        i, j = 1, 0
        n = len(arr)
       
        platforms = maxi = 1
       
        while i < n and j < n:
            if arr[i] <= dep[j]:
               platforms += 1
               i += 1
            else:
                platforms -= 1
                j += 1
            
            maxi = max(maxi, platforms)
        
        return maxi