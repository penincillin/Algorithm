/*
Bricks Falling When Hit, https://leetcode.com/problems/bricks-falling-when-hit/
The idea is to first remove all hitted bricks. Then sequentially adding these bricks back.
During this process, the bricks that can be recoverred is the erased bricks.
Refer to this solution: https://leetcode.com/problems/bricks-falling-when-hit/discuss/119829/Python-Solution-by-reversely-adding-hits-bricks-back
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
    int N, M;
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

    int dfs(vector<vector<int>>& grid, vector<vector<int>>& queue){
        int res = 0;
        while(queue.size() > 0){
            vector<int> top = queue[0]; queue.erase(queue.begin());
            int i = top[0], j = top[1];
            int i0, j0;
            for(int k=0; k<4; k++){
                extend(i, j, k, i0, j0);
                if (i0>0 && i0<N && j0>=0 && j0<M && grid[i0][j0]==1){
                    grid[i0][j0] = 2;
                    queue.push_back({i0, j0});
                    res += 1;
                }
            }
        }
        return res;
    }

    bool is_connected(vector<vector<int>> &grid, int i, int j){
        bool is_top = (i == 0);
        bool is_connect = false;
        for(int k=0; k<4; k++){
            int i0, j0;
            extend(i, j, k, i0, j0);
            is_connect |= (i0>=0 && i0<N && j0>=0 && j0<M && grid[i0][j0]==2);
        }
        return is_top | is_connect;
    }
public:
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        N = grid.size(), M = grid[0].size(); // N is the 

        for(auto hit : hits){
            int i=hit[0], j=hit[1];
            grid[i][j] = grid[i][j]==1 ? 0 : -1;
        }

        vector<vector<int>> queue;
        for(int j=0; j<M; j++){
            if(grid[0][j] == 1){
                queue.push_back({0, j});
                grid[0][j] = 2;
            }
        }
        int mid_res = dfs(grid, queue);

        vector<int> res;
        reverse(hits.begin(), hits.end());
        int count = 0;
        for(auto hit : hits){
            cout << count << " " << hits.size() << "\n";
            count++;
            int i=hit[0], j=hit[1];
            if (grid[i][j] == 0){
                grid[i][j] = 1;
                bool is_connect = is_connected(grid, i, j);
                cout << i << " " << j << " " << is_connect << "\n";
                if (is_connected(grid, i, j)){
                    grid[i][j] = 2;
                    queue.push_back({i, j});
                    int mid_res = dfs(grid, queue);
                    res.push_back(mid_res);
                }
                else{
                    res.push_back(0);
                }
            }
            else{
                res.push_back(0);
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};

int main(){
    vector<vector<int>> grid, hits;
    grid = {{1,0,1,0}, {1,1,1,0}}; hits = {{0,0}, {0,2}};
    grid = {{1},{1},{1},{1},{1}}; hits = {{3,0},{4,0},{1,0},{2,0},{0,0}};


    Solution sol;
    vector<int> res = sol.hitBricks(grid, hits);
    print_vec(res);
    return 0;
}
