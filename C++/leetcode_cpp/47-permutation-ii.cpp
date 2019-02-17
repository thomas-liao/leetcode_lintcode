class Solution {
public:
    /*
     * @param :  A list of integers
     * @return: A list of unique permutations
     */
    vector<vector<int>> permuteUnique(vector<int> &nums) {
      vector<vector<int>> result;
      vector<bool> visited(nums.size(), false);
      vector<int> subset;
      // sort(nums, nums.begin(), nums.end()); @error, wrong expression
      sort(nums.begin(), nums.end());
      helper(nums, subset, visited, result);
      return result;
    }
    
    void helper(vector<int> &nums, vector<int> &subset, vector<bool> &visited, vector<vector<int>> &result) {
      if (nums.size() == subset.size()) {
        result.push_back(subset);
        return;
      }
      for (int i = 0; i < nums.size(); i++) {
        if (visited[i] || i > 0 && nums[i] == nums[i-1] && !visited[i-1]){
          continue;
        }
        subset.push_back(nums[i]);
        visited[i] = true;
        helper(nums, subset, visited, result);
        visited[i] = false;
        subset.pop_back();
     }
    }
};
