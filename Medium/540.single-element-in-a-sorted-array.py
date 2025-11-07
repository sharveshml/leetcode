#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1

        while lo < hi:
            mid = (lo+hi) // 2

            if mid % 2 == 0:
                if nums[mid+1] == nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                if nums[mid - 1] == nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
        return nums[lo]

# a = Solution()
# a.singleNonDuplicate([1,1,2,3,3,4,4,8,8])

# @lc code=end

