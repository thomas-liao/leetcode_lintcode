// didn't pass, TLE later at extreme cases
// class Solution {
// public:
//     /**
//      * @param a: A 32bit integer
//      * @param b: A 32bit integer
//      * @param n: A 32bit integer
//      * @return: An integer
//      */
//     int fastPower(int a, int b, int n) {
//         // write your code here
        
//         //// @ error: with n < 3, sometimes the larger is too large causing bug
//         //// @ error: (double) a % b is wrong, invalid operands of type double....
//         // if (n < 3) {
//         //     // return (int)((long)pow(a, n) % b); // @ error: note, by default pow(a, b) return double
//         if (n == 0) {
//             // return 1; // @ error 4, 1%1?
//             return 1 % b;
//         }
//         if (n == 1) {
//             return a % b;
//         }
//         long long l = fastPower(a, b, n / 2);
//         long long r = fastPower(a, b, n - n / 2); // this seems to be a waste.. it can go faster
//         return (l % b)*(r % b) % b;
//     }
// };



class Solution {
public:
    /**
     * @param a: A 32bit integer
     * @param b: A 32bit integer
     * @param n: A 32bit integer
     * @return: An integer
     */
    int fastPower(int a, int b, int n) {
        if (n == 0) {
            return 1 % b;
        }
        if (n == 1) {
            return a % b;
        }
        long long temp = fastPower(a, b, n / 2);
        if (n % 2 == 0) {
            return (temp % b)*(temp % b)%b;
        } else {
            return (temp%b) * (temp*a%b) % b;
        }
    }
};






























