class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        if s is None:
            return []
        if len(s) == 0:
            return []
        if len(s) < 2:
            return [s]
        result = []
        self.backtrack(s, 0, result)
        return result
    
    # @error: string.find("xxx", start) instead of list.find...(invalid)
    def backtrack(self, s, start, result):
        idx = s.find("++", start)
        if idx == -1:
            return
        s = list(s)
        s[idx] = s[idx+1] = '-'
        result.append(''.join(s))
        s[idx] = s[idx+1] = '+'
        self.backtrack(''.join(s), idx + 1, result)
