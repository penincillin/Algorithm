#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <assert.h>


using namespace std;

int abs(int num){
    if(num < 0) return -num;
    else        return num;
}

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
    int twoSumClosest(vector<int>& nums, int target){
        assert(nums.size() >= 2);
        int result = nums[0] + nums[nums.size()-1];
        int begin=0, end=nums.size()-1;
        while(end > begin){
            if((nums[end]+nums[begin]) >= target){
                if((nums[end]+nums[begin]) == target){
                    return target;
                }
                if(abs(nums[end]+nums[begin]-target) < abs(result-target))
                    result = nums[end]+nums[begin];
                int back_end = nums[end];
                while(back_end == nums[end] && end>0){
                    end --;
                }
            }
            else{
                if(abs(nums[end]+nums[begin]-target) < abs(result-target))
                    result = nums[end]+nums[begin];
                int back_begin = nums[begin];
                while(back_begin == nums[begin] && begin<int(nums.size()-1)){
                    begin ++;
                }
            }
        }
        return result;
    }

    int threeSumClosest(vector<int>& nums, int target) {
        int result = nums[0]+nums[1]+nums[2];   
        sort(nums.begin(), nums.end());
        vector<int> back_nums = nums;
        int prefix = 0;
        for(unsigned i=0; i<nums.size()-2; i++){
            int two_target = target-nums[i];
            back_nums.erase(back_nums.begin());
            if(i>0 && two_target==prefix) continue;
            else prefix = two_target;
            int two_result = twoSumClosest(back_nums, two_target);
            if(abs(two_result+nums[i]-target) < abs(result-target))
                result = two_result+nums[i];
        }
        return result;
    }
};

int main(){
    Solution ss;
    //int A[15] = {-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6};
    //vector<int> nums(A, A+15);
    int A[4] = {-1, 2, 1, -4};
    vector<int> nums(A, A+4);
    sort(nums.begin(), nums.end());
    printVec(nums);
    cout << ss.threeSumClosest(nums, 1) << endl;
    return 0;
}
