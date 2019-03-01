# solution 1
class Solution(object):
    res = None
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        assert num >= 0
        self.process(num)
        return self.res
        
    def process(self, num):
        # if num %10 == 0: # wrong
        if num < 10:
            self.res = num
            return
        sum_ = 0
        while num:
            sum_ += num % 10
            num //= 10
        self.process(sum_)
            
        
