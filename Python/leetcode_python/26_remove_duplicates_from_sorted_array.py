# #1 
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         idx = 0
#         for i in range(len(nums)):
#             if i == 0:
#                 idx += 1
#                 continue
#             if nums[i] != nums[i-1]:
#                 nums[idx] = nums[i]
#                 idx += 1
#             else:
#                 continue
#         return idx

# 2
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
        return idx
