# brute force O(N^3), TLE
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         n = len(nums)
        
#         if len(set(nums)) < 3:
#             return False
#         for i in range(n - 2):
#             for j in range(i+1, n):
#                 for k in range(j + 1, n):
#                     if nums[i] < nums[k] < nums[j]:
#                         return True
#         return False
                

# still TLE....  whatever pass
# solution , O(N^2) - lower and upper bound method, slide j and find k (i is abstract into stored_min) # efficiently find lower bound
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        n = len(nums)
        stored_min = [0 for _ in range(n)]
        min_ = nums[0]
        for i in range(n):
            min_ = min(min_, nums[i])
            stored_min[i] = min_
        
        for j in range(1, n - 1):
            lower = stored_min[j-1]
            upper = nums[j]
            for k in range(j + 1, n):
                if lower < nums[k] < upper:
                    return True
        return False
