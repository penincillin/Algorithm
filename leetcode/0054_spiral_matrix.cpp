/*
 * Spiral Matrix: https://leetcode.com/problems/spiral-matrix/
 */
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;

        if (matrix.size() == 0){
            return res;
        }

        int left=0, right=matrix[0].size()-1; // [left, right]
        int upper=0, down=matrix.size()-1; // [upper, down]
        
        while(left <= right && upper <= down){
            // left to right
            for(int i=left; i<=right; i++){
                res.push_back(matrix[upper][i]);
            }
            upper++;
            if (upper > down){
                break;
            }

            // upper to down
            for(int i=upper; i<=down; i++){
                res.push_back(matrix[i][right]);
            }
            right--;
            if (left > right){
                break;
            }

            // right to left
            for(int i=right; i>=left; i--){
                res.push_back(matrix[down][i]);
            }
            down--;
            if (upper > down){
                break;
            }

            // down to upper
            for(int i=down; i>=upper; i--){
                res.push_back(matrix[i][left]);
            }
            left++;
            if (left > right){
                break;
            }

        }

        return res;
    }
};

template <typename T>
void print_vec(vector<T> vec){
    for(int i=0; i<vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << "\n";
}

int main(){
    vector<int> row1{1, 2, 3, 4};
    vector<int> row2{5, 6, 7, 8};
    vector<int> row3{9, 10, 11, 12};
    //print_vec<int>(row1);

    vector<vector<int>> matrix;
    matrix.push_back(row1);
    matrix.push_back(row2);
    matrix.push_back(row3);

    Solution sol;
    vector<int> res = sol.spiralOrder(matrix);
    print_vec(res);

    return 0;
}
