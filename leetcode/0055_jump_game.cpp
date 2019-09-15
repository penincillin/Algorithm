#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_idx = 0;
        auto array_len = nums.size();
        for (auto i=0; i<array_len; i++){
            if (max_idx>=i) {
                if (i==array_len-1){
                    return true;
                }
                max_idx = max(max_idx, i+nums[i]);
                if (max_idx>=array_len-1){
                    return true;
                }
            }
            else{
                return false;
            }
        }
        return false;
    }
};

int main(){
    int A[] = {2,3,1,1,4};
	int n = sizeof(A) / sizeof(A[0]);
	vector<int> nums(A, A + n);
    
    Solution solution;
    bool res = solution.canJump(nums);
    cout << res << endl;
    return 0;
}
