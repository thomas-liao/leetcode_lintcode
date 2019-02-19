# solution 1, O(n), with extra space
# class Solution:
#     """
#     @param: nums: an array of integers
#     @return: the number of unique integers
#     """
#     def deduplication(self, nums):
#         seen = set()
#         idx = 0
        
#         for i in range(len(nums)):
#             if nums[i] not in seen:
#                 seen.add(nums[i])
#                 nums[idx] = nums[i]
#                 idx += 1;
#         return idx;

# solution 2, O(nlogn) without extra space
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if not nums:
            return 0
        nums.sort()
        idx = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
        return idx
