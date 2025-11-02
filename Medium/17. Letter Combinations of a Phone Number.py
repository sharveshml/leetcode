class Solution:
    def backtrack(self, i, digitChars, digits, ans, res):
        if len(ans) == len(digits):
            res.append(ans)
            return res
        
        for c in digitChars[digits[i]]:
            self.backtrack(i+1, digitChars, digits, ans+c, res)
        
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        digitChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        return self.backtrack(0,digitChars, digits, "", [])