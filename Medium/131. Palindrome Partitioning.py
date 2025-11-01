class Solution:
    def isPalindrome(self, start, end, s):
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True
    def recurse(self, ind, s, tmp, res):
        if ind == len(s):
            res.append(tmp[:])
        
        for i in range(ind, len(s)):
            if self.isPalindrome(ind, i, s):
                tmp.append(s[ind:i+1])
                self.recurse(i+1, s, tmp, res)
                tmp.pop()


    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.recurse(0, s, [],res)
        return res