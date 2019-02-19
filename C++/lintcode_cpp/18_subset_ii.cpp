class Solution {
public:
    /**
     * @param nums: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    vector<vector<int>> subsetsWithDup(vector<int> &nums) {
        // write your code here
        if (nums.empty()) {
            return vector<vector<int>> {{}};
        }
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        vector<int> subset;
        dfs(nums, subset, result, 0);
        return result;
    }
    
    void dfs(vector<int> &nums, vector<int> &subset, vector<vector<int>> &result, int start) {
        result.push_back(subset);
        for (int i = start; i < nums.size(); i++) {
            if (i != start && nums[i] == nums[i-1]) continue;
            subset.push_back(nums[i]);
            dfs(nums, subset, result, i + 1);
            subset.pop_back();
        }
    }
};
