class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, maxi = 0, -1000000

        for i in nums:
            sum += i

            maxi = max(maxi, sum)

            if sum < 0:
                sum = 0

        return maxi