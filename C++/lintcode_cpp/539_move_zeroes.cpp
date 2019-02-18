class Solution {
public:
    /**
     * @param nums: an integer array
     * @return: nothing
     */
    void moveZeroes(vector<int> &nums) {
        // write your code here
        int idx = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) continue; // keep finding non-zero value
            int temp = nums[i];
            nums[i] = nums[idx];
            nums[idx] = temp;
            idx++;
        }
    }
};
