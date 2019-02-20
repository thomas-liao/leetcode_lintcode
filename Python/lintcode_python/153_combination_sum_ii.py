# dfs + backtracking   
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):   
        if not num:
            return []
        num.sort()
        result = []
        self.dfs(num, target, 0, 0, [], result)
        return result
    
    def dfs(self, num, target, start, sum_, subset, result):
        if sum_ > target:
            return
        if sum_ == target:
            result.append(subset.copy())
        
        for i in range(start, len(num)):
            if i != start and num[i] == num[i-1]:
                continue
            sum_ += num[i]
            subset.append(num[i])
            self.dfs(num, target, i + 1, sum_, subset, result)
            sum_ -= num[i]
            subset.pop()
