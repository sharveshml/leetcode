class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()

        for num in nums:
            hashSet.add(num)
        
        print(dir(hashSet))
        maxi = 0

        for num in hashSet:
            count = 0

            if num + 1 not in hashSet:
                curNum = num
                count = 1

                while curNum - 1 in hashSet:
                    count += 1
                    curNum -= 1

            maxi = max(maxi, count)

        return maxi