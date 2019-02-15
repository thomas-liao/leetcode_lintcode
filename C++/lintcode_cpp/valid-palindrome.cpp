//2-14
class Solution {
public:
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    bool isPalindrome(string &s) {
        // write your code here
        int i = 0, j = s.length() - 1;
        while (i < j) {
            while (i < s.length() && !isalnum(s[i])) {
                i++;
            }
            while (j >= 0 && !isalnum(s[j])) {
                j--;
            }
            if (tolower(s[i]) != tolower(s[j])) {
                return false;
            }
            j--;
            i++;
        }
        return true;
    }
};
