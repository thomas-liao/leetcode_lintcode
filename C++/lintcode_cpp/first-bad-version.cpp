/**
 * class SVNRepo {
 *     public:
 *     static bool isBadVersion(int k);
 * }
 * you can use SVNRepo::isBadVersion(k) to judge whether 
 * the kth code version is bad or not.
*/
class Solution {
public:
    /**
     * @param n: An integer
     * @return: An integer which is the first bad version.
     */
    int findFirstBadVersion(int n) {
        // write your code here
        int left = 1, right = n;
        int mid;
        while (left + 1 < right) {
            mid = left + (right - mid) / 2;
            if (SVNRepo::isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid;
            }
        }
        if (SVNRepo::isBadVersion(left)) return left;
        return right;
    }
};
