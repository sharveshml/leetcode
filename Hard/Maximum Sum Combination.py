# Given two integer arrays nums1 and nums2 and an integer k, return the maximum k valid sum combinations from all possible sum combinations using the elements of nums1 and nums2.



# A valid sum combination is made by adding one element from nums1 and one element from nums2. Return the answer in non-increasing order.


# Examples:
# Input: nums1 = [7, 3], nums2 = [1, 6], k = 2

# Output: [13, 9]

# Explanation:

# The 2 maximum combinations are made by:

# nums1[0] + nums2[1] = 13

# nums1[1] + nums2[1] = 9
import heapq
class Solution():
    def maxSumCombination(self, nums1, nums2, k):
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)

        max_heap = []
        visited = set()
        res = []

        heapq.heappush(max_heap, (-(nums1[0]+nums2[0]), 0, 0))
        visited.add(0,0)

        while k > 0 and max_heap:
            curr_sum, i, j = heapq.heappop(max_heap)
            res.append(curr_sum)
            k -= 1

            if i+1 < len(nums1) and (i+1,j) not in visited:
                heapq.heappush(-(nums1[i+1]+nums2[j]), i+1, j)
                visited.add(i+1, j)
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(-(nums1[i]+nums2[j+1]),i,j+1)
                visited.add(i, j+1)
        
        return res
