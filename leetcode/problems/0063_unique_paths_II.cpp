/* Unique Paths II, https://leetcode.com/problems/unique-paths-ii/
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
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid.size() == 0 || obstacleGrid[0].size() == 0){
            return 0;
        }
        else{
            int m = obstacleGrid.size();
            int n = obstacleGrid[0].size();
            int res[m][n];
            memset(res, 0, m*n*4);
            if (!obstacleGrid[0][0]){
                res[0][0] = 1;
            }
            for(int i=0; i<m; i++){
                for(int j=0; j<n; j++){
                    if (!obstacleGrid[i][j]){
                        if (i-1 >= 0){
                            res[i][j] += res[i-1][j];
                        }
                        if (j-1 >= 0){
                            res[i][j] += res[i][j-1];
                        }
                    }
                }
            }
            return res[m-1][n-1];
        }
    }
};


int main(){
    vector<int> vec1{0, 0, 0};
    vector<int> vec2{0, 1, 0};
    vector<vector<int>> grid{vec1, vec2, vec1};
    Solution sol;
    int res = sol.uniquePathsWithObstacles(grid);
    cout << res << "\n";
    return 0;
}
