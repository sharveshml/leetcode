class Solution:
    def recurse(self, ind, nums, path, result):
        result.append(path[:])

        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i-1]:
                continue
            
            path.append(nums[i])
            self.recurse(i+1, nums, path, result)
            path.pop()


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        self.recurse(0, nums, [], res)

        return res