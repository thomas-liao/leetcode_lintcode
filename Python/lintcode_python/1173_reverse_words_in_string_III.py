# solution 1, most straightforward solution
class Solution:
    """
    @param s: a string
    @return: reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
    """
    def reverseWords(self, s):
        # Write your code here
        s_list = s.strip().split()
        new_s_list = []
        for word in s_list:
            word = self.rev(word)
            new_s_list.append(word)
        return " ".join(new_s_list)

    def rev(self, word):
        word = list(word)
        left, right = 0, len(word) - 1
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return ''.join(word)
