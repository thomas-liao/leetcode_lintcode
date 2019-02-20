class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if candidates is None:
            return []
        candidates = list(set(candidates)) # de-duplication
        candidates.sort()
        result = []
        self.dfs(candidates, target, 0, 0, [], result)
        return result;
    
    def dfs(self, candidates, target, sum_, start, subset, result):
        if sum_ > target:
            return
        if sum_ == target:
            result.append(subset.copy())
        
        for i in range(start, len(candidates)):
            sum_ += candidates[i]
            subset.append(candidates[i])
            self.dfs(candidates, target, sum_, i, subset, result)
            subset.pop()
            sum_ -= candidates[i]
