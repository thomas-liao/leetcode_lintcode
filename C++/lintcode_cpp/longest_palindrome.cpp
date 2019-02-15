class Solution {
public:
    /**
     * @param s: a string which consists of lowercase or uppercase letters
     * @return: the length of the longest palindromes that can be built
     */
    int longestPalindrome(string &s) {
        // write your code here
        vector<int> freqs (128, 0);
        int ans = 0;
        for (const char c : s) {
            ++freqs[c];
        }
        int odd = 0;
        for (const int freq : freqs) {
            if (freq == 0) {continue;}
            ans += freq / 2 * 2;
            if (freq % 2 == 1) {
                odd = 1;
            }
        }
        return ans + odd;
    }
};
