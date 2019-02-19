// modify original data - dfs
// class Solution {
// public:
//     int numIslands(vector<vector<char>>& grid) {
//         if (grid.empty()) return 0;
        
//         int res = 0, m = grid.size(), n = grid[0].size();
//         for (int i = 0; i < m; i++) {
//             for (int j = 0; j < n; j++) {
//                 if (grid[i][j] == '0') continue;
//                 res++;
//                 eraser(grid, i, j);
//             }
//         }
//         return res;
//     }
       
//     void eraser(vector<vector<char>>& grid, int i, int j) { // dfs eraser
//         int m = grid.size(), n = grid[0].size();
//         // base case
//         if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') {
//             return;
//         }
//         grid[i][j] = '0';
//         eraser(grid, i, j + 1);
//         eraser(grid, i, j - 1);
//         eraser(grid, i - 1, j);
//         eraser(grid, i + 1, j);
//     }
// };

//TLE ???? why
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        int m = grid.size(), n = grid[0].size();
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    res++;
                    bfs(grid, i, j);
                }
            }
        }
        return res;
    }
    
    void bfs(vector<vector<char>>&grid, int i, int j) {
        int m = grid.size(), n = grid[0].size();
        queue<pair<int, int>> q;
        q.push({i, j});
        
        int dx[4] = {-1, 1, 0, 0};
        int dy[4] = {0, 0, -1, 1};
        while (!q.empty()) {
            pair<int, int> p = q.front();
            q.pop();
            grid[p.first][p.second] = '0'; // erase
            
            for (int k = 0; k < 4; k++) {
                pair<int, int> nei = {p.first + dx[k], p.second + dy[k]};
                int x = nei.first, y = nei.second;
                if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == '0') {
                    continue;
                }
                q.push({nei.first, nei.second});
            }
        }
    }
};
