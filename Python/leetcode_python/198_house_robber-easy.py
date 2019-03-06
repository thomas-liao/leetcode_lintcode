class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dp[i]: maximum I can get if robbed here
        if not nums or len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        n = len(nums)
        dp = [0 for _ in range(n)]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
        return dp[n-1]
