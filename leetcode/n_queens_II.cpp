/*
 * N-Queens-II, https://leetcode.com/problems/n-queens-ii/
 * DFS and backtrace.
 */

#include <iostream>
#include <string>
#include <vector>
#include <string.h>
using namespace std;

class Solution {
public:

    void solve(int &res, bool *row, bool *col, bool *diag, int sum, int depth, int n){
        if (depth == n*n){ 
            if (sum == n){
                res += 1;
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
                solve(res, row, col, diag, sum+1, depth+1, n);
                row[i] = 0;
                col[j] = 0;
                diag[d0] = 0;
                diag[d1] = 0;
            }
            solve(res, row, col, diag, sum, depth+1, n);
        }
    }

    int totalNQueens(int n){
        int res = 0;
        if (n == 0){
            return res;
        }

        bool row[n];
        bool col[n];
        bool diag[4*n-2];
        memset(row, 0, n);
        memset(col, 0, n);
        memset(diag, 0, (4*n-2));

        solve(res, row, col, diag, 0, 0, n);
        return res; 
    }
};

int main(){
    Solution sol;
    int n = 4;
    int res = sol.totalNQueens(n);
    cout << "res " << res << "\n";
    return 0;
}
