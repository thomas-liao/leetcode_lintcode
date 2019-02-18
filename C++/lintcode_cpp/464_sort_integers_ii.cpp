// // solution1, quicksort
// psedo code:
// quickSort(arr[], low, high)
// {
//     if (low < high)
//     {
//         /* pi is partitioning index, arr[pi] is now
//           at right place */
//         pi = partition(arr, low, high);

//         quickSort(arr, low, pi - 1);  // Before pi
//         quickSort(arr, pi + 1, high); // After pi
//     }
// }
// class Solution {
// public:
//     /**
//      * @param A: an integer array
//      * @return: nothing
//      */
//     void sortIntegers2(vector<int> &A) {
//         // write your code here
//         quickSort(A, 0, A.size() - 1);
//     }
    
//     void quickSort(vector<int> &A, int left, int right) {
//         if (left < right) {
//             int idx = partition(A, left, right, (left+right)/2);
//             quickSort(A, left, idx - 1);
//             quickSort(A, idx + 1, right);
//         }
//     }
    
//     // do not miss out the left, right in partition!!!!!!!!!!1
//     // set idx = left instead of 0!!!!
//     int partition(vector<int> &A, int left, int right, int pivot) {
//         int val = A[pivot];
//         swap(A, pivot, right);
//         int idx = left;
//         for (int i = left; i <= right; i++) {
//             if (A[i] < val) {
//                 swap(A, idx, i);
//                 idx++;
//             }
//         }
//         swap(A, idx, right);
//         return idx;
//     }
    
//     void swap(vector<int> &A, int a, int b) {
//         int temp = A[a];
//         A[a] = A[b];
//         A[b] = temp;
//     }
// };


// Solution 2, merge sort
// MergeSort(arr[], l,  r)
// If r > l
//      1. Find the middle point to divide the array into two halves:  
//              middle m = (l+r)/2
//      2. Call mergeSort for first half:   
//              Call mergeSort(arr, l, m)
//      3. Call mergeSort for second half:
//              Call mergeSort(arr, m+1, r)
//      4. Merge the two halves sorted in step 2 and 3:
//              Call merge(arr, l, m, r)
class Solution {
public:
    /**
     * @param A: an integer array
     * @return: nothing
     */
    void sortIntegers2(vector<int> &A) {
        mergeSort(A, 0, A.size() - 1);
    }
    
    void mergeSort(vector<int> &A, int left, int right) {
        // base case: 0 or 1 element in array, return
        if (left < right) {
            int mid = (left + right) / 2;
            // divide
            mergeSort(A, left, mid);
            mergeSort(A, mid + 1, right);
            merge(A, left, right, mid);
        }
    }
    
    void merge(vector<int> &A, int left, int right, int mid) {
        int i = left, j = mid + 1, k = 0, temp[right-left+1];
        while (i <= mid && j <= right) {
            if (A[i] < A[j]) {
                temp[k] = A[i];
                i++;
            } else {
                temp[k] = A[j];
                j++;
            }
            k++;
        }
        while (i <= mid) {
            temp[k++] = A[i++];
        }
        while (j <= right) {
            temp[k++] = A[j++];
        }
        for (int i = left; i <= right; i++) {
            A[i] = temp[i-left];
        }
    }
};
