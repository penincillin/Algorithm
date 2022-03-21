/* 39. Combination Sum. https://leetcode.com/problems/combination-sum/
 * The idea is recursive and the most important thing is that starting from current position instead of the begining of the array
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
private:
    typedef vector<vector<int>> res_data;
    vector<int> remove_redunc(vector<int>& candidates){
        vector<int> nums;
        if (candidates.size()<1){
            return nums;
        }
        int previous_num = candidates[0];
        nums.push_back(candidates[0]);
        for(int i=1; i<candidates.size(); i++){
            if (candidates[i] != previous_num){
                nums.push_back(candidates[i]);
                previous_num = candidates[i];
            }
        }
        return nums;
    }
    unordered_map<int, res_data> solutions;
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> nums = remove_redunc(candidates);
        return _combinationSum(nums, 0, target);
    }

    vector<vector<int>> _combinationSum(vector<int>& nums, int start, int target){
        vector<vector<int>> res;
        if (target<0){
            return res;
        }
        if (target==0){
            vector<int> empty_res;
            res.push_back(empty_res);
            return res;
        }
        for(int i=start; i<nums.size(); i++){
            if (nums[i] <= target){
                vector<vector<int>> mid_res = _combinationSum(nums, i, target-nums[i]); // important, starts from i instead of 0
                for(int j=0; j<mid_res.size(); j++){
                    vector<int> tmp_res = mid_res[j];
                    tmp_res.push_back(nums[i]);
                    res.push_back(tmp_res);
                }
            }
        }
        return res;
    }


    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
		vector< vector< vector<int> > > combinations(target + 1, vector<vector<int>>());
		combinations[0].push_back(vector<int>());
		for (auto& score : candidates)
			for (int j = score; j <= target; j++)
				if (combinations[j - score].size() > 0)	{
					auto tmp = combinations[j - score];
					for (auto& s : tmp)
						s.push_back(score);
					combinations[j].insert(combinations[j].end(), tmp.begin(), tmp.end());
				}
		auto ret = combinations[target];
		
		return ret;
	}
};


int main(){
    //vector<int> candidates = {2,3,6,7}; int target = 7;
    vector<int> candidates = {2,3,5}; int target = 8;
    Solution solution;
    vector<vector<int>> res = solution.combinationSum(candidates, target);
    for(int i=0; i<res.size(); i++){
        for(int j=0; j<res[i].size(); j++){
            cout << res[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
