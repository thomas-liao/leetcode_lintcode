class Solution {
public:
    /**
     * @param num: a positive integer
     * @return: if num is a perfect square else False
     */
    bool isPerfectSquare(int num) {
        // write your code here
        if (num < 0) return false;
        int left = 0, right = num;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            // long temp = mid * mid; // here is mistake, error: long temp = (long) mid * mid!!!!!
            long temp = (long) mid * mid;
            if (temp == num) return true;
            if (temp < num) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
};
