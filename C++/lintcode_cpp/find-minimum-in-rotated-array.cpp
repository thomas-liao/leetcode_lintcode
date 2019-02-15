// note, you will have to do comparison with nums[right], otherwise if you compare wiht nums[start]
// then when the array is completely sorted like [1, 2, 3] it will cause bug.
class Solution {
public:
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    int findMin(vector<int> &nums) {
        // write your code here
        int left = 0, right = nums.size() - 1;
        int mid;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return min(nums[left], nums[right]);
    }
};
