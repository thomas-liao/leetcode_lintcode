# too slow..
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         idx = []
#         vowels = []
#         s = list(s)
#         for i in range(len(s)):
#             c = s[i]
#             if self.isVowel(c):
#                 idx.append(i)
#                 vowels.append(c)
#         print(vowels)
        
#         self.reverse_(vowels)
#         print("revsed: ", vowels)
#         counter = 0
#         for i in idx:
#             s[i] = vowels[counter]
#             counter += 1
#         return ''.join(s)
        
#     def isVowel(self, c):
#         #if c in set(['a', 'e', 'i', 'o', 'u', 'y']): # wrong... upper letter? lower letter?
#         if c.lower() in set(['a', 'e', 'i', 'o', 'u']):
#             return True
#         return False
    
#     def reverse_(self, list_):
#         if not list:
#             return 
#         start, end = 0, len(list_) - 1
#         while start < end:
#             list_[start], list_[end] = list_[end], list_[start]
#             start += 1
#             end -= 1

# two pointers
class Solution:
    def reverseVowels(self, s: str) -> str:
        if not str:
            return str
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.isVowel(s[i]):
                i += 1
            while i < j and not self.isVowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
            
            i += 1
            j -= 1
        return ''.join(s)
    
    def isVowel(self, c):
        if c.lower() in set(['a', 'e', 'i', 'o', 'u']):
            return True
        return False
 
