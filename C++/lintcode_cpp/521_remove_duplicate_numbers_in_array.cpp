class Solution {
public:
    /**
     * @param nums: an array of integers
     * @return: the number of unique integers
     */
    int deduplication(vector<int> &nums) {
        // write your code here
        if (nums.size() < 2) return nums.size();
        sort(nums.begin(), nums.end());
        int idx = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i-1]) {
                nums[idx] = nums[i];
                idx++;
            }
        }
        return idx;
    }
};
