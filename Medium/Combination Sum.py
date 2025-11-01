class Solution:
    def recurse(self, ind, candidates, sum, target, tmp, res):

        if sum > target:
            return

        if ind == len(candidates) or sum == target:
            if sum == target:
                res.append(tmp[:])
            return
        
        tmp.append(candidates[ind])
        self.recurse(ind, candidates, sum+candidates[ind], target, tmp, res)
        tmp.pop()
        self.recurse(ind+1, candidates, sum, target, tmp, res)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        self.recurse(0, candidates, 0, target, [], res)

        return res