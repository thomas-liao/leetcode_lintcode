class Solution {
public:
    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    int sqrt(int x) {
        // write your code here
        if (x < 0) throw "Invalid input";
        if (x == 0) return 0;
        int left = 0, right = x;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if ((long)mid * mid <= x) {
                left = mid;
            } else {
                right = mid;
            }
        }
        if ((long)right*right <= x) return right;
        return left;
    }
};
