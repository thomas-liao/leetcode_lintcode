// didn't pass... didn't handle overflow
// i.e. int: -(-2^31) overflows to -2^31, instead of 2^31
// we can use long to prevent this from happening

// class Solution {
// public:
//     /**
//      * @param x: the base number
//      * @param n: the power number
//      * @return: the result
//      */
//     double myPow(double x, int n) {
//         // write your code here
//         bool isNegative = false;
//         if (x < 0) isNegative = true;
//         if (n < 0) {
//             n = -n;
//             x = 1.0 / x;
//         }
//         double temp = myPowHelper(x, n);
//         if (isNegative) {
//             temp = -temp;
//         }
//         return temp;
//     }
//     double myPowHelper(double x, int n) {
//         if (x == 0 && n == 0) throw "0 to the power of 0 is invalid!";
//         if (n == 0) return 1.0;
//         if (n == 1) return x;
//         long double temp = myPow(x, n / 2);
//         if (n % 2 == 0) {
//             return temp * temp;
//         } else {
//             return temp * temp * x;
//         }
//     }
// };




// prevent overflow version - recursion
class Solution {
public:
    /**
     * @param x: the base number
     * @param n: the power number
     * @return: the result
     */
    double myPow(double x, int n) {
        if (x == 0 && n == 0) throw "Invalid input!";
        if (x == 0) return 0;
        if (n == 0) return 1.0;
        bool isNegative = false;
        if (x < 0) {
            isNegative = true;
            x = - x;
        }
        long m = n;
        if (n < 0) {
            x = 1 / x;
            m = -m; // prevent overflow, i.e. -(-2^31) overflows to (-2^31) instead of 2^31
        }
        double temp = myPowHelper(x, m);
        if (isNegative) {
            temp = -temp;
        }
        return temp;
    }
    
    double myPowHelper(double x, long m) {
        if (m == 0) return 1.0;
        if (m == 1) return x;
        long double temp = myPowHelper(x, m / 2);
        if (m % 2 == 0) {
            return temp * temp;
        } else {
            return temp * temp * x;
        }
    }
};
