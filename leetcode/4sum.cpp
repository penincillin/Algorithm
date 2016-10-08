#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void printVecs(vector<vector<int>> results){
    for(unsigned i=0; i<results.size(); i++){
        for(unsigned j=0; j<results[i].size(); j++){
            cout << results[i][j] << " ";
        }
        cout << endl;
    }
}
void printVec(vector<int> vec){
    for(unsigned i=0; i<vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << endl;
}

class Solution {
public:
    vector<vector<int>> twoSum(vector<int> &nums, int target){
        vector<vector<int>> results;
        int begin=0, end=nums.size()-1;
        while(end > begin){
            if((nums[end]+nums[begin]) >= target){
                if((nums[end]+nums[begin]) == target){
                    vector<int> mid_res;
                    mid_res.push_back(nums[begin]);
                    mid_res.push_back(nums[end]);
                    results.push_back(mid_res);
                }
                int back_end = nums[end];
                while(back_end == nums[end] && end>0) 
                    end--;
            }
            else{
                int back_begin = nums[begin];
                while(back_begin == nums[begin] && begin<int(nums.size()-1))
                    begin++;
            }
        }
        return results;
    }

    vector<vector<int>> threeSum(vector<int>& nums, int target) {
        vector<vector<int>> results;
        vector<int> back_nums = nums;
        int prefix = 0;
        for(unsigned i=0; i<nums.size(); i++){
            int new_target = target-nums[i];
            if(i>0 && new_target==prefix) {
                back_nums.erase(back_nums.begin());
                continue;
            }
            else { 
                prefix = new_target;
                back_nums.erase(back_nums.begin());
            }
            vector<vector<int>> two_res = twoSum(back_nums, new_target);
            if(two_res.size() > 0){
                for(unsigned j=0; j<two_res.size(); j++){
                    two_res[j].push_back(target-new_target);
                    results.push_back(two_res[j]);
                }
            }
        }
        return results;
    }

     vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        vector<int> back_nums = nums;
        int prefix = 0;
        for(unsigned i=0; i<nums.size(); i++){
            int new_target = target-nums[i];
            if(i>0 && new_target==prefix) {
                back_nums.erase(back_nums.begin());
                continue;
            }
            else { 
                prefix = new_target;
                back_nums.erase(back_nums.begin());
            }
           vector<vector<int>> three_res = threeSum(back_nums, new_target);
           if(three_res.size() > 0){
               for(unsigned j=0; j<three_res.size(); j++){
                    three_res[j].push_back(target-new_target);
                    results.push_back(three_res[j]);
                }
            }
        }
        return results;
    }
};

int main(){
    Solution ss;
    int A[15] = {1, 0, -1, 0, -2, 2};
    vector<int> nums(A, A+6);
    vector<vector<int>> results = ss.fourSum(nums, 0);
    printVecs(results);
    return 0;
}

