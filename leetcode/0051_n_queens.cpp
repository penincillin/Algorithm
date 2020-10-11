/*
 * N-Queens, https://leetcode.com/problems/n-queens/
 * DFS and backtrace.
 */

#include <iostream>
#include <string>
#include <vector>
#include <string.h>
using namespace std;

class Solution {
public:

    void solve(vector<vector<string>> &res, bool *row, bool *col, bool *diag, bool *board, int sum, int depth, int n){
        if (depth == n*n){ 
            if (sum == n){
                vector<string> mid_res;
                for(int i=0; i<n; i++){
                    string s = "";
                    for(int j=0; j<n; j++){
                        if (board[i*n+j]){
                            s += "Q";
                        }
                        else{
                            s += ".";
                        }
                    }
                    mid_res.push_back(s);
                }
                res.push_back(mid_res);
            }
        }
        else{
            int i = depth % n;
            int j = depth / n;
            int d0 = (i+j);
            int d1 = j + (n-1)-i + (2*n-1);
            if (!row[i] && !col[j] && !diag[d0] && !diag[d1]){
            //if (!row[i] && !col[j]){
                row[i] = 1;
                col[j] = 1;
                diag[d0] = 1;
                diag[d1] = 1;
                board[depth] = 1;
                solve(res, row, col, diag, board, sum+1, depth+1, n);
                row[i] = 0;
                col[j] = 0;
                diag[d0] = 0;
                diag[d1] = 0;
                board[depth] = 0;
            }
            solve(res, row, col, diag, board, sum, depth+1, n);
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        if (n == 0){
            return res;
        }

        bool board[n*n];
        bool row[n];
        bool col[n];
        bool diag[4*n-2];
        memset(board, 0, n*n);
        memset(row, 0, n);
        memset(col, 0, n);
        memset(diag, 0, (4*n-2));

        solve(res, row, col, diag, board, 0, 0, n);
        return res; 
    }
};

int main(){
    Solution sol;
    int n = 4;
    vector<vector<string>> res = sol.solveNQueens(n);
    for(int i=0; i<res.size(); i++){
        for(int j=0; j<res[i].size(); j++){
            cout << res[i][j] << "\n";
        }
        cout << "-----------------\n";
    }
    return 0;
}
