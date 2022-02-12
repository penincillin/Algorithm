/*
Count Square Submatrices with All Ones, https://leetcode.com/problems/count-square-submatrices-with-all-ones/
The brutal-fource idea is to use accumulating sum, and check every possibility for every element.
This problem can be solved in dp, where dp[i][j] refers to the number of squares that use i, j as the right-bottom points.
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <string>
#include <map>
#include <unordered_map>
#include <set>
#include <array>
#include <queue>
using namespace std;

template<typename T>
void print_array(T A[], int size){
    for(int i=0; i<size; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

template <typename T>
void print_vec(vector<T> vec){
    for(auto v:vec){
        cout << v << " ";
    }
    cout << "\n";
}

class Solution {
private:
    int count[300][300];
    int M, N;

    int obtain_sum(int i, int j){
        return i>=0 && j>=0 ? count[i][j] : 0;
    }

    void calc_cum_sum(vector<vector<int>>& matrix){
        M = matrix.size();
        N = matrix[0].size();
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                int sum0 = obtain_sum(i-1, j-1);
                int sum1 = obtain_sum(i, j-1);
                int sum2 = obtain_sum(i-1, j);
                count[i][j] = sum1 + sum2 - sum0 + matrix[i][j];
            }
        }
    }

    int get_square_sum(int i0, int j0, int i1, int j1){
        int sum0 = obtain_sum(i0-1, j0-1);
        int sum1 = obtain_sum(i0-1, j1);
        int sum2 = obtain_sum(i1, j0-1);
        int sum3 = obtain_sum(i1, j1);
        return sum3 + sum0 - sum2 - sum1;
    }

public:
    Solution() {
        for(int i=0; i<300; i++){
            for(int j=0; j<300; j++){
                count[i][j] = 0;
            }
        }
    }
    int countSquares(vector<vector<int>>& matrix) {
        return solve_dp(matrix);
    }

    int solve_dp(vector<vector<int>>& matrix) {
        int dp[301][301] = {0};
        int res = 0;
        M = matrix.size(); N = matrix[0].size();
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                if (matrix[i][j] == 1){
                    if(i==0 || j==0){
                        dp[i][j] = 1;
                    }
                    else{
                        dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
                    }
                    res += dp[i][j];
                }
            }
        }
        return res;
    }

    int solve_brutal(vector<vector<int>>& matrix) {
        calc_cum_sum(matrix);

        int res = 0;
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                int K = (int)min(M-i, N-j);
                for(int k=1; k<=K; k++){
                    int square_sum = get_square_sum(i, j, i+k-1, j+k-1);
                    if (square_sum == k * k){
                        res += 1;
                    }
                }
            }
        }
        return res;
    }
};

int main(){
    vector<vector<int>> matrix;
    matrix = { {0,1,1,1}, {1,1,1,1}, {0,1,1,1}, };

    Solution sol;
    int res = sol.countSquares(matrix);
    cout << res << "\n";
    return 0;
}