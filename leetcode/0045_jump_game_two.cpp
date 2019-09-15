// jump_method1 is the o(n^2) algorithm. Its idea is to calculate go to i-th idex requires at least how many steps
// Jump_method2 is the o(n) algorithm. Its idea is to calculate with 1 step, I can go to which indexes, then with 2 steps I can go to which steps. Then repeating this process, until go to the last index.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:

    int jump_method1(vector<int>& nums) {
        auto array_len = nums.size();
        int min_jumps[array_len];   
        for (int i=0; i<array_len; i++){
            min_jumps[i] = 0;
        }
        for (auto i=0; i<array_len; i++){
            int num_jump = nums[i];
            //cout << "i: " << i << " num_jump: " << num_jump << "\n";
            for (int j=i+1; j<i+1+num_jump && j<array_len; j++){
                //cout << "j: " << j << " min_jumps: " << min_jumps[j] << "\n";
                if (min_jumps[j] == 0){
                    min_jumps[j] = min_jumps[i]+1;
                }
                else{
                    min_jumps[j] = min(min_jumps[j],min_jumps[i]+1);
                }
            }
        }
        return min_jumps[array_len-1];
    }

    int jump_method2(vector<int>& nums) {
        auto array_len = nums.size();
        int begin_idx=0, end_idx=0;
        int max_step=0;
        while(begin_idx<array_len-1 && end_idx<array_len){
            int max_idx = end_idx;
            for(int i=begin_idx; i<end_idx+1; i++){
                max_idx = max(max_idx, nums[i]+i);
            }
            max_step += 1;
            if (max_idx>=array_len-1){
                break;
            }
            else{
                begin_idx = end_idx+1;
                end_idx = max_idx;
            }
        }
        return max_step;
    }
};

int main(){
    //int A[] = {2,3,1,1,4};
    //int A[] = {0};
    //int A[] = {1,2};
    int A[] = {5,9,3,2,1,0,2,3,3,1,0,0};
	int n = sizeof(A) / sizeof(A[0]);
	vector<int> nums(A, A + n);
    
    Solution solution;
    int res = solution.jump(nums);
    cout << res << endl;
    return 0;
}
