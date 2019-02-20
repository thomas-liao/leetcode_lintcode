# 2-19-19
# related: subsetII, permutation II... pay attension to the detailed difference
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if digits is None or len(digits) ==0:
            return []
        dict_ = {}
        dict_['2'] = "abc"
        dict_['3'] = "def"
        dict_['4'] = "ghi"
        dict_['5'] = "jkl"
        dict_['6'] = "mno"
        dict_['7'] = "pqrs"
        dict_['8'] = "tuv"
        dict_['9'] = "wxyz"
        result = []
        self.dfs(digits, dict_, 0, [], result)
        return result

    def dfs(self, digits, dict_, index, subset, result):
        if (index == len(digits)):
            result.append(''.join(subset))
            return
            
        for c in dict_[digits[index]]:
            subset.append(c)
            self.dfs(digits, dict_, index + 1, subset, result)
            subset.pop()
