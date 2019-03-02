# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        counter = 0
        while True:
            counter += 1
            if counter >= 1000:
                break
            mid = left + (right - left) // 2
            status = guess(mid)
            if status == 0:
                return mid
            if status == -1:
                right = mid - 1
            else:
                left = mid + 1
        else:
            raise Exception("Error: maximum count reached, not found!")
