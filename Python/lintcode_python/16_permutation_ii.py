class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        if nums is None or len(nums) == 0:
            return []
        result = []
        nums.sort()
        self.dfs(nums, [], result, [False for _ in range(len(nums))])
        return result
        
    def dfs(self, nums, subset, result, visited):
        if len(nums) == len(subset):
            # result.append(copy.deepcopy(subset)) # python2
            result.append(subset.copy()) # python3
            return
        
        for i in range(len(nums)):
            if visited[i] or i != 0 and nums[i] == nums[i-1] and not visited[i-1]:
                # illegal visit will occur
                continue
            visited[i] = True
            subset.append(nums[i])
            self.dfs(nums, subset, result, visited)
            visited[i] = False
            subset.pop()
