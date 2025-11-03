# TLE
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1

        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = -n

        for i in range(n):
            ans *= x

        return ans

# Optimized ( Law of Exponents )
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1

        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = -n

        while n > 0:

            if n % 2 != 0:
                result *= x

            x *= x
            n //=  2

        return result

a = Solution()
print(a.myPow(2,6))
