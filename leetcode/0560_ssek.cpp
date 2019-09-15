#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    // O(n^2)
    int subarraySum_slow(vector<int>& nums, int k) {
        int n = nums.size();
        int sum = 0;
        int res = 0;
        for (int i=0; i<n; i++){
            for(int j=i; j<n; j++){
                if (i==j){
                    sum = nums[j];
                }
                else{
                    sum += nums[j];
                }
                if (sum == k){
                    res += 1;
                }
            }
        }
        return res;
    }

    // O(n), use the idea of sum(i,j) = sum(0,j)-sum(0,i) and the idea of hash map
    int subarraySum(vector<int>& nums, int k){
        int n = nums.size();
        unordered_map<int, int> sum_dict;
        int res = 0;
        int sum = 0;
        sum_dict[0] = 1; // stands for the empty string or the start of the array
        for (int i=0; i<n; i++){
            sum += nums[i];
            auto count = sum_dict.count(sum-k);
            // be aware: update the res first then update the sum_dict
            if (count > 0){
                res += sum_dict[sum-k];
            }
            if (sum_dict.count(sum) <= 0){
                sum_dict[sum] = 1;
            }
            else{
                sum_dict[sum] += 1;
            }
        }
        return res;
    }
};

int main(){
    /*
    int k = 2;
    vector<int> nums = {1,1,1};
    int k = 0;
    vector<int> nums = {0,0,0,0,0};
    */
    int k = 0;
    vector<int> nums = {-1, -1, 1};
    Solution solution;
    int res = solution.subarraySum(nums, k);
    cout << res << "\n";
    return 0;
}
