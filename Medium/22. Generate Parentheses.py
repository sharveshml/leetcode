class Solution:
    def f(self, open, close, n, up, res):
        if len(up) == 2*n:
            res.append(up)
            return

        if open < n:
            self.f(open+1, close, n, up+'(', res)
        if close < open:
            self.f(open, close+1, n, up+')', res)


    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.f(0, 0, n, "", res)

        return res