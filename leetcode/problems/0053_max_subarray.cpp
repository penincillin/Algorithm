#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

class Solution {
public:
    int dp(vector<int>& nums) {
        int n = nums.size();
        //int *res = new int[n*n];
        int res[n];
        int max_value = nums[0];
        for(int l=1; l<=n; l++){
            for(int i=0; i<n-l+1; i++){
                int j=i+l-1;
                if (j-i>0){
                    res[i] = res[i] + nums[j];
                }
                else{
                    res[i] = nums[i];
                }
                max_value = max(res[i], max_value);
            }
        }
        return max_value;
    }

    int linear(vector<int>& nums){
        int res=nums[0];
        int cur=nums[0];
        for(int i=1; i<nums.size(); i++){
            cur += nums[i];
            if(nums[i] > cur){
                cur = nums[i];
            }
            res = max(res, cur);
        }
        return res;
    }

    int maxSubArray(vector<int>& nums){
        return linear(nums);
    }
};

int main(){
    vector<int> nums{1, 2};
    Solution sol;
    int res = sol.maxSubArray(nums);
    cout << res << "\n";
    return 0;
}
