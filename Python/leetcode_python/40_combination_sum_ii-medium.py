# solution 1... similar to subset II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target <= 0:
            return []
        result = []
        candidates = sorted(candidates)
        self.helper(candidates, target, 0, 0, [], result)
        return result
        
    def helper(self, candidates, target, start, sum_, subset, result):
        if sum_ == target:
            result.append(subset.copy())
            return
        if sum_ > target:
            return
        for i in range(start, len(candidates)):
            if i != start and candidates[i] == candidates[i-1]:
                continue
            subset.append(candidates[i])
            sum_ += candidates[i]
            self.helper(candidates, target, i + 1, sum_, subset, result)
            sum_ -= candidates[i]
            subset.pop()
        
            
