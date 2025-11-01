class Solution:
    def recurse(self, arr, ind, curr_sum, result):
        if ind == len(arr):
            result.append(curr_sum)
            return result

        self.recurse(arr, ind+1, curr_sum+arr[ind], result)
        self.recurse(arr, ind+1, curr_sum, result)

        return result

    def subsetSums(self, arr):
        result = []

        return self.recurse(arr, 0, 0, result)