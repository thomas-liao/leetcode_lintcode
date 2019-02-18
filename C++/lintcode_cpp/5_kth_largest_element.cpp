//// this solution is wrong although somehow it passed..
// class Solution {
// public:
//     /**
//      * @param n: An integer
//      * @param nums: An array
//      * @return: the Kth largest element
//      */
//     int kthLargestElement(int n, vector<int> &nums) {
//         // write your code here
//         int target_idx = nums.size() - n;
//         if (target_idx < 0) {
//             target_idx = 0;
//         }
//         int i = 0, j = nums.size() - 1;
//         while (i <= j) {
//             int idx = partition(nums, (i+j)/2);
//             if (idx == target_idx) {
//                 return nums[idx];
//             }
//             if (idx < target_idx) {
//                 i = idx + 1;
//             } else {
//                 j = idx - 1;
//             }
//         }
//     }
    
//     int partition(vector<int> &nums, int pivot) {
//         int value = nums[pivot];
//         swapElements(nums, pivot, nums.size() - 1); // swapped with rightmost element
//         int idx = 0;
//         for (int i = 0; i < nums.size() - 1; i++) {
//             if (nums[i] < value) {
//                 swapElements(nums, i, idx);
//                 idx++;
//             }
//         }
//         swapElements(nums, idx, nums.size() - 1); // swap back and put pivot val in the right place
//         return idx;
//     }
    
//     void swapElements(vector<int> &nums, int a, int b) {
//         int temp = nums[a];
//         nums[a] = nums[b];
//         nums[b] = temp;
//     }
    
// };


// corrected solution: 
class Solution {
public:
    /**
     * @param n: An integer
     * @param nums: An array
     * @return: the Kth largest element
     */
    int kthLargestElement(int n, vector<int> &nums) {
        int target_idx = nums.size() - n;
        if (target_idx < 0) target_idx = 0;
        int left = 0, right = nums.size() - 1;
        while (true) {
            int idx = partition(nums, left, right, (left + right) / 2);
            if (idx == target_idx) return nums[target_idx];
            if (idx < target_idx) {
                left = idx + 1;
            } else {
                right = idx - 1;
            }
        }
    }
    
    int partition(vector<int> &nums, int left, int right, int pivot) {
        int val = nums[pivot];
        swap(nums, pivot, right);
        // int idx = 0; @error
        int idx = left;
        for (int i = left; i < right; i++) {
            if (nums[i] < val) {
                swap(nums, i, idx);
                idx++;
            }
        }
        swap(nums, idx, right);
        return idx;
    }
    
    void swap(vector<int> &nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
};
