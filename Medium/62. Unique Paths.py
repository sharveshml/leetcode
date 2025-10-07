# Recursion - TLE
class Solution:
    def findUniquePaths(self, i: int, j: int, n: int, m: int) -> int:
        if i, j == n-1, m-1: 
            return 1
        
        if i >= n or j >= m:
            return 0

        right = down = 0
        right = self.findUniquePaths(i, j+1, n, m)
        down = self.findUniquePaths(i+1, j, n, m)

        return right+down

    def uniquePaths(self, m: int, n: int) -> int:
        return self.findUniquePaths(0,0,n,m)

# DP - Memoization
class Solution:
    def findUniquePaths(self, i: int, j: int, n: int, m: int, dp: List[List[int]]) -> int:
        if i, j == n-1, m-1: 
            return 1
        
        if i >= n or j >= m:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        right = down = 0
        right = self.findUniquePaths(i, j+1, n, m, dp)
        down = self.findUniquePaths(i+1, j, n, m, dp)

        dp[i][j] = right+down
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.findUniquePaths(0,0,n,m,dp)