class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in map.keys():
                return [map[diff], i]
            else:
                map[nums[i]] = i
        
        return [0,0]