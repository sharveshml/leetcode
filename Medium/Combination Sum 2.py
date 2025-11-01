class Solution:
    def recurse(self, ind, cur_sum, candidates, target, tmp, res):
        if cur_sum > target:
            return

        if cur_sum == target:
            res.append(tmp[:])
            return

        if ind == len(candidates):
            if cur_sum == target:
                res.append(tmp[:])
            return
        
        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i-1]:
                continue
            
            tmp.append(candidates[i])
            self.recurse(i+1, cur_sum+candidates[i], candidates, target, tmp, res)
            tmp.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.recurse(0, 0, candidates, target, [], res)

        return res