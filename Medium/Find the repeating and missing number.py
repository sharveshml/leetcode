class Solution:
    def findMissingRepeatingNumbers(self, nums):
        i = 0
        duplicate, missing = 0, 0
        tmp = []

        while i < len(nums):
            correct = nums[i] - 1

            if nums[i] != i-1:
                if nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                else:
                    duplicate = nums[i]
                    break
            else:
                i += 1
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1 and nums[i] - nums[i-1] != 0:
                missing = nums[i]+1
        
        tmp.append(duplicate)
        tmp.append(missing)

        return tmp