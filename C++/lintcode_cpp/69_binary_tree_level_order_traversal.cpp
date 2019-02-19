/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

// class Solution {
// public:
//     /**
//      * @param root: A Tree
//      * @return: Level order a list of lists of integer
//      */
//     vector<vector<int>> levelOrder(TreeNode * root) {
//         // write your code here
//         vector<vector<int>> result;
//         if (root == NULL) return result;
//         queue<TreeNode *> q; // error, originally wrote queue<TreeNode> q.... which is wrong, this his pointer!
//         q.push(root);
//         while (!q.empty()) {
//             int n = q.size();
//             vector<int> subset;
            
//             for (int i = 0; i < n; i++) {
//                 TreeNode *cur = q.front(); // similarly, it is TreeNode * instead of TreeNdoe
//                 q.pop();
//                 subset.push_back(cur -> val);
//                 if (cur -> left != NULL) {
//                     q.push(cur -> left);
//                 }
//                 if (cur -> right != NULL) {
//                     q.push(cur -> right);
//                 }
//             }
//             result.push_back(subset);
//         }
//         return result;
//     }
// };


// practice again

class Solution {
public:
    /**
     * @param root: A Tree
     * @return: Level order a list of lists of integer
     */
    vector<vector<int>> levelOrder(TreeNode * root) {
        vector<vector<int>> result;
        if (root == NULL) return result;
        queue<TreeNode *> q;
        q.push(root);
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> subset;
            for (int i = 0; i < size; i++) {
                TreeNode *cur = q.front(); q.pop();
                subset.push_back(cur -> val);
                if (cur -> left != NULL) {
                    q.push(cur -> left);
                }
                if (cur -> right != NULL) {
                    q.push(cur -> right);
                }
            }
            result.push_back(subset);
        }
        return result;
    }
};
