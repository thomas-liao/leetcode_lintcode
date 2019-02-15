class Solution {
public:
    /**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
    int search(vector<int> &A, int target) {
        // write your code here
        if (A.size() == 0) return -1; // forgot this one causing bug
        int left = 0, right = A.size() - 1;
        int mid;
        while (left + 1 < right) {
            // identify wihch segment we are at
            mid = left + (right - left) / 2;
            if (A[mid] > A[right]) {
                if (A[left] <= target && target <= A[mid]) {
                    right = mid;
                } else {
                    left = mid;
                }
            } else {
                if (A[mid] <= target && target <= A[right]) {
                    left = mid;
                } else {
                    right = mid;
                }
            }
            
        }
        if (A[left] == target) return left;
        if (A[right] == target) return right;
        return -1; // not found
    }
};
