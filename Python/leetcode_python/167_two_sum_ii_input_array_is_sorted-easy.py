class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) < 2:
            return [-1, -1]
        i, j = 0, len(numbers) - 1
        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                return [i+1, j+1]
            if sum_ < target:
                i += 1
            else:
                j -= 1
        return [-1, -1]
        
