/*
Shortest Path in a Grid with Obstacles Elimination, https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
BFS + DP
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

class Info{
public:
    int i, j, k;
    Info(int i, int j, int k){
        this->i = i;
        this->j = j;
        this->k = k;
    }
};

class Solution {
private:
    void extend(int i, int j, int to, int &i0, int &j0){
        if (to == 0){ // extend to upper
            i0 = i-1; j0 = j;
        }
        else if (to == 1){ // extend to left
            i0 = i; j0 = j-1;
        }
        else if (to == 2){ // extend to righ
            i0 = i; j0 = j+1;
        }
        else{ // extend to lower
            i0 = i+1; j0 = j;
        }
    }
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        return solve_dp(grid, k);        
    }

    int solve_dp(vector<vector<int>>& grid, int k){
        queue<Info> queue;
        const int M = grid.size();
        const int N = grid[0].size();
        const int K = k;
        const int MAX = M * N * 10;
        int dp[M][N][K+1]; // dp[i][j][k] means the smallest step taken to (i, j) with less than or equal to k elimination
        // init dp to max;
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                for(int k=0; k<=K; k++){
                    dp[i][j][k] = MAX;
                }
            }
        }
        // init start point
        for(int k=0; k<=K; k++){
            dp[0][0][k] = 0;
        }

        queue.push(Info(0, 0, 0)); // i, j, k, k means number of elimination performed
        while(queue.size() > 0){
            Info cur = queue.front(); queue.pop();
            int i0 = cur.i, j0 = cur.j, k0 = cur.k;
            int i, j;
            for(int to=0; to<4; to++){
                extend(i0, j0, to, i, j);
                if (i>=0 && i<M && j>=0 && j<N){
                    int k = k0 + (grid[i][j]==1);
                    if ((grid[i][j]==1 && k<=K) || grid[i][j]==0){
                        if (dp[i][j][k] > dp[i0][j0][k0]+1){
                            queue.push(Info(i, j, k));
                            for(int k_=k; k_<=K; k_++){
                                dp[i][j][k_] = min(dp[i0][j0][k0]+1, dp[i][j][k_]); // bug
                            }
                        }
                    }
                }
            }
        }

        int res = MAX;
        for(int k=0; k<=K; k++){
            res = min(res, dp[M-1][N-1][k]);
        }
        return res < MAX ? res : -1;
    }
};


int main(){
    vector<vector<int>> grid;
    int k;

    grid = {{0,0,0}, {1,1,0}};
    // grid = {{0,0,0}};
    grid = {{0,0,0},{1,1,0},{0,0,0},{0,1,1},{0,0,0}};
    k = 1;

    Solution sol;
    int res = sol.shortestPath(grid, k);
    cout << res << "\n";
    return 0;
}
