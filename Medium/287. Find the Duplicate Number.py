# Brute Force
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            map[num] = map.get(num,0)+1

        for i, j in map.items():
            if j > 1:
                return  i
        
        return 0

# Optimal Approach Cyclic Sort
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            correct = nums[i]-1

            if nums[i] != i+1:
                if nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                else:
                    return nums[i]
            else:
                i += 1
        return -1
            