/*
Valid Square, https://leetcode.com/problems/valid-square/
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;

void print_vec(vector<int> vec){
    for(auto v:vec){
        cout << v << " ";
    }
    cout << "\n";
}

class Solution {
private:
    vector<vector<int>> get_all_permutations(int n){
        vector<int> init_array;
        for(int i=0; i<n; i++){
            init_array.push_back(i);
        }
        vector<vector<int>> res;
        res.push_back(init_array);
        while(next_permutation(init_array.begin(), init_array.end())){
            res.push_back(init_array);
        }
        return res;
    }

    bool check_equal_length(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        int l1 = (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]);
        int l2 = (p2[0]-p3[0])*(p2[0]-p3[0]) + (p2[1]-p3[1])*(p2[1]-p3[1]);
        int l3 = (p3[0]-p4[0])*(p3[0]-p4[0]) + (p3[1]-p4[1])*(p3[1]-p4[1]);
        int l4 = (p4[0]-p1[0])*(p4[0]-p1[0]) + (p4[1]-p1[1])*(p4[1]-p1[1]);
        return l1==l2 and l2==l3 and l3==l4 and l1>0;
    }

    bool check_orthog(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        vector<vector<int>> ps = {p1, p2, p3, p4};
        for(int i=0; i<4; i++){
            int j = (i+1)%4, k = (i+2)%4;
            vector<int> vec1 = {ps[i][0]-ps[j][0], ps[i][1]-ps[j][1]};
            vector<int> vec2 = {ps[j][0]-ps[k][0], ps[j][1]-ps[k][1]};
            if ( (vec1[0]*vec2[0] + vec1[1]*vec2[1]) != 0 ){
                return false;
            }
        }
        return true;
    }

public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        vector<vector<int>> all_perms = get_all_permutations(4);
        vector<vector<int>> inputs = {p1, p2, p3, p4};
        for (auto idxs : all_perms){ 
            // vector<int> idxs
            vector<int> pp1 = inputs[idxs[0]];
            vector<int> pp2 = inputs[idxs[1]];
            vector<int> pp3 = inputs[idxs[2]];
            vector<int> pp4 = inputs[idxs[3]];
            bool equal_length = check_equal_length(pp1, pp2, pp3, pp4);
            if (equal_length){
                bool orthogonal = check_orthog(pp1, pp2, pp3, pp4);
                if (orthogonal){
                    return true;
                }
            }
        }
        return false;
    }
};

int main(){
    // vector<int> p1={0, 0}, p2={1, 1}, p3={1, 0}, p4={0, 1};
    // vector<int> p1={0, 0}, p2={1, 1}, p3={1, 0}, p4={0, 12};
    vector<int> p1 = {1,0}, p2 = {-1,0}, p3 = {0,1}, p4 = {0,-1};
    Solution sol;
    bool res = sol.validSquare(p1, p2, p3, p4);
    cout << res << "\n";
    return 0;
}
