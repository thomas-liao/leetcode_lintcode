# solution 1... kind of cheating
# from collections import Counter
# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         if not nums or len(nums) < 2:
#             return []
#         counter = Counter(nums)
#         res = []
#         for k, v in counter.items():
#             if v == 2:
#                 res.append(k)
#         return sorted(res)
    
# solution 2, O(nlogn) time, without extra space

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         if not nums or len(nums) < 2:
#             return []
#         nums = sorted(nums)
#         res = []
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i+1]:
#                 res.append(nums[i])
#         return res
