/* Unique Paths, https://leetcode.com/problems/unique-paths/
 * Simplest DP.
 */
#include <iostream>
#include <string.h>
#include <string>
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
    int uniquePaths(int m, int n) {
        if (m==0 || n==0){
            return 1;
        }
        int res[m][n];
        memset(res, 0, 4*m*n);
        res[0][0] = 1;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i-1>=0){
                    res[i][j] += res[i-1][j];
                }
                if(j-1>=0){
                    res[i][j] += res[i][j-1];
                }
            }
        }
        return res[m-1][n-1];
    }
};


int main(){
    int m = 3, n = 7;
    Solution sol;
    int res = sol.uniquePaths(m, n);
    cout << res << "\n";
    return 0;
}
