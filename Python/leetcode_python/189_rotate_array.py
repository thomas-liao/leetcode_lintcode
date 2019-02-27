# solution 1
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k, n = k % len(nums), len(nums)
#         self.reverse(nums, 0, n - k - 1)
#         self.reverse(nums, n - k, n - 1)
#         self.reverse(nums, 0, n - 1)
        
#     def reverse(self, nums, start, end):
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start += 1
#             end -= 1
            
# solution 2:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k is None or k <= 0:
            return
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k] # correct
        # @ error nums[:] = nums[-k:] + nums[:n-k] # bug: [1] 1 - > [1, 1]
