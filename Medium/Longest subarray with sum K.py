class Solution:
    def longestSubarray(self, nums, k):
        hashmap = {0: -1}
        prefixSum = 0
        maxLength = 0

        for i in range(len(nums)):
            prefixSum += nums[i]

            if prefixSum - k in hashmap:
                maxLength = max(maxLength, i-hashmap[prefixSum-k])
            
            hashmap[prefixSum] = i
        
        return maxLength