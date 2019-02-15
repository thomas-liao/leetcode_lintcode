
// template 1
// class Solution {
// public:
//     /**
//      * @param A: An integers array.
//      * @return: return any of peek positions.
//      */
//     int findPeak(vector<int> &A) {
//         // write your code here
//         int left = 1, right = A.size() - 2;
//         int mid;
//         // bug: if left < right, missing one value.
//         while (left <= right) {
//             mid = left + (right - left) / 2;
//             if (A[mid] > A[mid-1] && A[mid] > A[mid+1]) {
//                 return mid;
//             }
//             if (A[mid] < A[mid-1]) {
//                 right = mid - 1;
//             } else {
//                 left = mid + 1;
//             }
//         }
//         return -1;
//     }
// };


// template 3: extereme fool-proof
class Solution {
public:
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    int findPeak(vector<int> &A) {
        int left = 1, right = A.size() - 2;
        int mid;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (A[mid] > A[mid-1] && A[mid] > A[mid+1]) {
                return mid;
            }
            if (A[mid] < A[mid-1]) {
                right = mid;
            } else {
                left = mid;
            }
        }
        if (A[left] > A[left-1] && A[left] > A[left+1]) return left;
        return right;
        
    }
};
        
        
        
        
        
        
