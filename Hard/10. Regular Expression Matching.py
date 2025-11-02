# Recursive
class Solution:
    def recurse(self, i, j, s, p):
        # Base case: both exhausted
        if i < 0 and j < 0:
            return True

        # Pattern exhausted but string not
        if j < 0 and i >= 0:
            return False

        # String exhausted, but pattern remains
        if i < 0:
            # pattern can still match if it's like a*b*c*
            while j >= 0:
                if p[j] == '*':
                    j -= 2  # skip 'x*' pair
                else:
                    return False
            return True

        # Normal match or '.'
        if s[i] == p[j] or p[j] == '.':
            return self.recurse(i - 1, j - 1, s, p)

        # '*' case
        if p[j] == '*':
            # Option 1: zero occurrence of p[j-1]
            zero_case = self.recurse(i, j - 2, s, p)

            # Option 2: one or more occurrence, if current char matches p[j-1]
            one_or_more = False
            if j > 0 and (s[i] == p[j - 1] or p[j - 1] == '.'):
                one_or_more = self.recurse(i - 1, j, s, p)

            return zero_case or one_or_more

        # No match
        return False

    def isMatch(self, s: str, p: str) -> bool:
        return self.recurse(len(s) - 1, len(p) - 1, s, p)

# Memoization

class Solution:
    def recurse(self, i, j, s, p, dp):
        if i < 0 and j < 0:
            return True
        
        if (i,j) in dp:
            return dp[(i,j)]

        if j < 0 and i >= 0:
            return False

        if i < 0:
            while j >= 0:
                if p[j] == '*':
                    j -= 2
                else:
                    return False
            return True

        if s[i] == p[j] or p[j] == '.':
            return self.recurse(i - 1, j - 1, s, p, dp)

        if p[j] == '*':
            zero_case = self.recurse(i, j - 2, s, p, dp)

            one_or_more = False
            if j > 0 and (s[i] == p[j - 1] or p[j - 1] == '.'):
                one_or_more = self.recurse(i - 1, j, s, p, dp)

            dp[(i,j)] =  zero_case or one_or_more
        else:
            dp[(i,j)] = False

        return dp[(i,j)]

    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        return self.recurse(len(s) - 1, len(p) - 1, s, p, dp)