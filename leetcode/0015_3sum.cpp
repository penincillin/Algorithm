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

    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        vector<int> back_nums = nums;
        int prefix = 0;
        for(unsigned i=0; i<nums.size(); i++){
            int target = -nums[i];
            if(i>0 && target==prefix) {
                back_nums.erase(back_nums.begin());
                continue;
            }
            else { 
                prefix = target;
                back_nums.erase(back_nums.begin());
            }
            vector<vector<int>> two_res = twoSum(back_nums, target);
            if(two_res.size() > 0){
                for(unsigned j=0; j<two_res.size(); j++){
                    two_res[j].push_back(-target);
                    results.push_back(two_res[j]);
                }
            }
        }
        return results;
    }
};

int main(){
    Solution ss;
    int A[15] = {-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6};
    vector<int> nums(A, A+15);
    vector<vector<int>> results = ss.threeSum(nums);
    printVecs(results);
    return 0;
}
