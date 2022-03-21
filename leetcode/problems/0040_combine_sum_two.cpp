/* 40. Combination Sum II. https://leetcode.com/problems/combination-sum-ii/
 * Similar to Problem 39. And the key idea is to skip the number number
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        return _combinationSum(candidates, 0, target);
    }
    vector<vector<int>> _combinationSum(vector<int>& nums, int start, int target){
        vector<vector<int>> res;
        if (target==0){
            vector<int> empty_res;
            res.push_back(empty_res);
            return res;
        }
        int previous_num = -1; // use previous_num to ensure the repeated number is overlooked
        for(int i=start; i<nums.size(); i++){
            if (nums[i] <= target && nums[i]>previous_num){
                previous_num = nums[i];
                if (target-nums[i]>=0){
                    vector<vector<int>> mid_res = _combinationSum(nums, i+1, target-nums[i]);
                    for(int j=0; j<mid_res.size(); j++){
                        vector<int> tmp_res = mid_res[j];
                        tmp_res.push_back(nums[i]);
                        res.push_back(tmp_res);
                    }
                }
            }
        }
        return res;
    }

    
};


int main(){
    //vector<int> candidates = {10,1,2,7,6,1,5}; int target=8;
    vector<int> candidates = {1,2,2,2,5}; int target=5;
    Solution solution;
    vector<vector<int>> res = solution.combinationSum2(candidates, target);
    for(int i=0; i<res.size(); i++){
        for(int j=0; j<res[i].size(); j++){
            cout << res[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
