// class Solution {
// public:
//     /**
//      * @param x: a double
//      * @return: the square root of x
//      */
//     double sqrt(double x) {
//         // write your code here
//         if (x < 0) throw "Invalid input of x!";
//         double left = 0;
//         double right = x < 1? 1.0 : x;
        
//         // wrong, should be abs
//         // while ((long double) left*left - x > 1e-6) {
//         while (abs((long double) left*left - x) > 1e-10) {
//             double mid = left + (right - left) / 2;
//             if ((long double)mid*mid < x) {
//                 left = mid;
//             } else {
//                 right = mid;
//             }
//         }
//         return left;
//     }
// };


// Newton's method.. the abs((long double)... thing is causing TLE but.. whatever
class Solution {
public:
    /**
     * @param x: a double
     * @return: the square root of x
     */
    double sqrt(double x) {
        if (x < 0) throw "Invalid input";
        double result = x / 2; // randomly guess a value
        while (abs((long double) result*result - x) > 1e-12) {
            result = (result / 2 + x / (2*result)); // some math..
        }
        return result;
    }
};
