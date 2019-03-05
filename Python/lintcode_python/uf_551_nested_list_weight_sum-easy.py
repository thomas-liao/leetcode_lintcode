#
# python solution without using the given stupid data structure....


class Solution:

    def weightedSum(self, nestedList):
        if not nestedList or len(nestedList) == 0:
            return None
        return self.helper(nestedList, 1)



    def helper(self, nestedList, depth):
        if nestedList is None or len(nestedList) == 0:
            return 0
        sum_ = 0

        for e in nestedList:
            if type(e) is int:
                sum_ += depth * e
            else:
                sum_ += depth * self.helper(e, depth + 1)
        return sum_

