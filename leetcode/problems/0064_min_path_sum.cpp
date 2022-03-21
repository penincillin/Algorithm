/* Minimum Path Sum, https://leetcode.com/problems/minimum-path-sum/submissions/
 *
 */
#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;

template <typename T>
void print_vec(vector<T> vec){
    for(int i=0; i<vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << "\n";
}

template <typename T>
void print_vec_II(vector<vector<T>> vec){
    for(int i=0; i<vec.size(); i++){
        for(int j=0; j<vec[i].size(); j++){
            cout << vec[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "------------------\n";
}

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0){
            return 0;
        }
        else{
            int m = grid.size();
            int n = grid[0].size();
            int res[m][n];
            memset(res, 0, m*n*4);
            for(int i=0; i<m; i++){
                for(int j=0; j<n; j++){
                    res[i][j] = grid[i][j];
                    bool updated = false;
                    if (i-1 >= 0){
                        res[i][j] = res[i-1][j] + grid[i][j];
                        updated = true;
                    }
                    if (j-1 >= 0){
                        if (updated){
                            res[i][j] = min(res[i][j], grid[i][j]+res[i][j-1]);
                        }
                        else{
                            res[i][j] = res[i][j-1] + grid[i][j];
                        }
                    }
                }
            }
            return res[m-1][n-1];
        }
    }
};


int main(){
    vector<int> v1{1, 3, 1};
    vector<int> v2{1, 5, 1};
    vector<int> v3{4, 2, 1};
    vector<vector<int>> grid{v1, v2, v3};
    Solution sol;
    int res = sol.minPathSum(grid);
    cout << res << "\n";
    return 0;
}
