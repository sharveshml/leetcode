#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def recurse(self, up, p, res):
        if up == "":
            res.append(p)
            return

        digit = ord(up[0]) - ord('0')
        start = (digit - 2)*3
        if digit > 7:
            start += 1
        end = start + 3

        if digit == 7 or digit == 9:
            end += 1
        
        for i in range(start, end):
            ch = chr(ord('a') + i)
            self.recurse(p+ch, up[1:], res)

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        self.recurse(digits, "", res)

        return res if len(res) > 0 else []
        
# @lc code=end

