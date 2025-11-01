# TLE
class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = []
        available_days = [True] * (max(deadline) + 1)
        total_profit = 0
        total_jobs = 0
        
        for i in range(len(profit)):
            jobs.append([i,deadline[i],profit[i]])
        
        jobs.sort(key=lambda x:x[2],reverse=True)
        
        for i in range(len(jobs)):
            job, deadline_val, profit_val = jobs[i]
            
            for day in range(min(max(deadline), deadline_val), 0, -1):
                if available_days[day]:
                    total_profit += profit_val
                    total_jobs += 1
                    available_days[day] = False
                    break
                
        return [total_jobs, total_profit]
    
# Optimized solution
class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = sorted(list(zip(deadline,profit)), key=lambda x:x[1], reverse=True)
        max_deadline = max(deadline)
        
        slots = [-1] * (max_deadline+1)
        total_profit = 0
        jobs_scheduled = 0
        
        for d, p in jobs:
            for t in range(d, 0, -1):
                if slots[t] == -1:
                    slots[t] = 1
                    total_profit += p
                    jobs_scheduled += 1
                    break
                
        return [jobs_scheduled, total_profit]
            
# Heap Solution
import heapq

class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = []
        max_deadline = max(deadline)
        
        for d, p in zip(deadline, profit):
            jobs.append((d,p))
            
        jobs.sort()
        
        total_profit = 0
        min_heap = []
        i = len(deadline) - 1
        job_count = 0
        
        for time in range(max_deadline, 0, -1):
            
            while i>=0 and jobs[i][0] >= time:
                heapq.heappush(min_heap, -jobs[i][1])
                i -= 1
            
            if min_heap:
                total_profit += -heapq.heappop(min_heap)
                job_count += 1
                
        
        return [job_count, total_profit]
            