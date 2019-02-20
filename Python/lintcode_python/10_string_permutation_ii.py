class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        if str is None:
            return []
        if len(str) == 0:
            return [""]
        str_ = sorted(list(str))
        result = []
        visited = [False for _ in range(len(str_))]
        self.dfs(str_, [], result, visited)
        return result
        
    def dfs(self, str_, subset, result, visited):
        if (len(subset) == len(str_)):
            result.append(''.join(subset))
            return
        
        for i in range(len(str_)):
            if visited[i] or i != 0 and str_[i] == str_[i-1] and not visited[i-1]:
                continue
            subset.append(str_[i])
            visited[i] = True
            self.dfs(str_, subset, result, visited)
            visited[i] = False
            subset.pop()
