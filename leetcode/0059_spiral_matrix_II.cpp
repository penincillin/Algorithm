/*
 * Spiral Matrix II, https://leetcode.com/problems/spiral-matrix-ii/
 */
#include <iostream>
#include <vector>
using namespace std;

template <typename T>
void print_vec(vector<vector<T>> vec){
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
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res_vec;    
        if (n == 0){
            return res_vec;
        }

        int res[n][n];
        int left=0, right=n-1, up=0, down=n-1;
        int cur = 1;
        int thresh = n * n;
        while(left <= right && up <= down){
            for(int i=left; i<=right; i++){
                res[up][i] = cur;
                cur++;
            }
            up++;
            if (cur > thresh) break;

            for(int i=up; i<=down; i++){
                res[i][right] = cur;
                cur++;
            }
            right--;
            if (cur > thresh) break;

            for(int i=right; i>=left; i--){
                res[down][i] = cur;
                cur++;
            }
            down--;
            if (cur > thresh) break;

            for(int i=down; i>=up; i--){
                res[i][left] = cur;
                cur++;
            }
            left++;
        }

        for(int i=0; i<n; i++){
            vector<int> mid_res(res[i], res[i]+n);
            res_vec.push_back(mid_res);
        }
        return res_vec;
    }
};

int main(){
    Solution sol;
    int n = 4;
    vector<vector<int>> res = sol.generateMatrix(n);
    print_vec(res);
    return 0;
}
