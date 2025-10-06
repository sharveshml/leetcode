# Brute Force
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i],0)+1
        
        for k,v in map.items():
            if v > len(nums) / 2:
                return k

# Optimized ( Boyer-Moore Voting Algorithm )
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for i in nums:
            if count == 0:
                candidate = i
            count += (1 if i == candidate else -1)
        return candidate