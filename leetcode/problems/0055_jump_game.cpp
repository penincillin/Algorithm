/*
 * Jump Game, https://leetcode.com/problems/jump-game/
 * The idea is to use greedy algorithm.
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int head = 0;
        int reach = 0;
        int len = nums.size();
        while (head < len && head <= reach){
            reach = max(reach, head+nums[head]);
            if (reach >= len-1){
                return true;
            }
            head ++;
        }
        return false;
    }
};

int main(){
    //vector<int> nums{0, 3, 1, 1, 4};
    vector<int> nums{3, 2, 1, 0, 4};
    Solution sol;
    bool res = sol.canJump(nums);
    cout << res << "\n";
}
