#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        maxi = 0

        for i in nums:
            hashSet.add(i)
        
        for i in nums:
            top = i
            count = 0
            while top in hashSet:
                count += 1
                top -=1

            maxi = max(maxi, count)
        
        return maxi
# @lc code=end

