class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        idx = 0
        counter = 0
        for i in range(len(nums)):
            if i == 0:
                counter += 1
                idx += 1
            elif counter >= 2 and nums[i] == nums[i-1]:
                continue
            elif counter < 2 and nums[i] == nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
                counter += 1
            elif nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                counter = 1
                idx += 1
            else:
                raise Exception("Shouldn't reach this else statement.")
        
        return idx
