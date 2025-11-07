class Solution:
    def recurse(self, nums, tmp, res):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        
        for i in range(0, len(nums)):
            if nums[i] in tmp:
                continue
            tmp.append(nums[i])
            self.recurse(nums, tmp, res)
            tmp.pop()
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.recurse(nums, [], res)
        return res