#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        
        for i in range(n-1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
        
        if carry > 0:
            digits.insert(0, carry)
            
        return digits
# @lc code=end