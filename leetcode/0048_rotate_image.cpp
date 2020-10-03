/* 48. Rotate Image. https://leetcode.com/problems/rotate-image/
 */

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int start_x=0, start_y=0, len=matrix.size();
        while (len>=1 && start_x < matrix.size()/2){
            for(int i=0; i<len-1; i++){
                int x = start_x;
                int y = start_y+i;
                int store_value = matrix[x][y];
                for(int j=0; j<4; j++){
                    int new_x = y;
                    int new_y = (matrix.size()-1-x);
                    int tmp = matrix[new_x][new_y];
                    matrix[new_x][new_y] = store_value;
                    store_value = tmp;
                    x = new_x;
                    y = new_y;
                }
            }
            start_x += 1;
            start_y += 1;
            len -= 2;
        }
    }
};

int main(){
    //vector<vector<int>> matrix {{1,2,3}, {4,5,6}, {7,8,9}};
    vector<vector<int>> matrix = {{ 5, 1, 9,11}, {2, 4, 8,10}, {13, 3, 6, 7}, {15,14,12,16}};
    Solution solution;
    solution.rotate(matrix);
    for (int i=0; i<matrix.size(); i++){
        for (int j=0; j<matrix.size(); j++){
            cout << matrix[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
