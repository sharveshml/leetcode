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
    

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        
        return [1] + digits
# @lc code=end