class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = sorted(list(set(candidates)))
        self.helper(candidates, target, 0, 0, [], result)
        return result
    
    def helper(self, candidates, target, sum_, start, subset, result):
        if sum_ == target:
            # result.append(subset)# wrong
            result.append(subset.copy())
            return
        if sum_ > target:
            return
        for i in range(start, len(candidates)):
            sum_ += candidates[i]
            subset.append(candidates[i])
            self.helper(candidates, target, sum_, i, subset, result)
            sum_ -= candidates[i]
            subset.pop()
        
