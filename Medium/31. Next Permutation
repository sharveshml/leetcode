# Pythonic Solution
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums)-2, len(nums)-1

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = len(nums)-1
            while j >=0 and nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = reversed(nums[i+1:])

# Converted Java Code

class Solution:
    def swap(self, a, b, lst):
        tmp = lst[a]
        lst[a] = lst[b]
        lst[b] = tmp
    
    def reverse(self, i, j, nums):
        while i<=j and i < len(nums) and j>=0:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

            i += 1
            j -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums)-2, len(nums)-1

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = len(nums)-1
            while j >=0 and nums[j] <= nums[i]:
                j -= 1
            
            self.swap(i,j,nums)

        self.reverse(i+1, len(nums)-1, nums)
