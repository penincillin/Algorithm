/*
 * Permutations: https://leetcode.com/problems/permutations/submissions/
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void print_vec(vector<int> vec){
    for (auto it = vec.begin(); it!=vec.end(); it++){
        cout << *it << " ";
    }
    cout << "\n";
}

class Solution {
public:
    void solve(vector<vector<int>> & res, vector<int> nums, int head, int tail){
        if (head>=tail-1){
            res.push_back(nums);
        }
        else{
            for(int i=head; i<tail; i++){
                swap(nums[head], nums[i]);
                solve(res, nums, head+1, tail);
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        //sort(nums.begin(), nums.end());
        solve(res, nums, 0, nums.size());
        return res;
    }
};

int main(){
    Solution sol;
    vector<int> nums{1, 2, 3};

    //sol.permute(nums);
    vector<vector<int>> res = sol.permute(nums);
    for (int i=0; i<res.size(); i++){
        print_vec(res[i]);
    }

    return 0;
}
