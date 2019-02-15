// Solution 1, O(N-k) time
// class Solution {
// public:
//     vector<int> findClosestElements(vector<int>& arr, int k, int x) {
//         int i = 0, j = arr.size() - 1;
//         while (j - i + 1 > k) {
//             if (abs(arr[i] - x) > abs(arr[j] - x)) {
//                 i++;
//             } else {
//                 j--;
//             }
//         }
//         return vector<int>(arr.begin() + i, arr.begin() + i + k);
//     }
// };


// Solution2, O(logN + k)
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int idx = firstNotSmallerThan(arr, x);     
        cout << idx << endl;
        if (idx == -1) {
            return vector<int>(arr.end() - k, arr.end());
        }
        if (idx == 0) {
            return vector<int>(arr.begin(), arr.begin() + k);
        }
        int left = idx - 1, right = idx;
        // select from range [left+1, right - 1]
        // total elements: right - 1 - (left + 1) + 1 = right - left - 1
        while (left != -1 && right != arr.size() && right - left - 1 < k) {
            if (abs(arr[left] - x) <= abs(arr[right] - x)) {
                left--;
            } else {
                right++;
            }
        }
        while (left == -1 && right - left - 1 < k) {
            right++;
        }
        while (right == arr.size() && right - left - 1 < k) {
            left--;
        }

        return vector<int>(arr.begin() + left + 1, arr.begin() + left + k + 1);
    }
    
    int firstNotSmallerThan(vector<int>&arr, int x) {
        int left = 0, right = arr.size() - 1;
        int mid;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (arr[mid] < x) {
                left = mid+1;
            } else {
                right = mid;
            }
        }
        if (arr[left] >= x) {
            return left;
        }
        if (arr[right] >= x) {
            return right;
        }
        return -1; // all elements >= x
    }
};









