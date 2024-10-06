/* Jump Game II, https://leetcode.com/problems/jump-game-ii/
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

class Solution {
public:
    int solve_slow(vector<int>& nums) {
        int len = nums.size();
        int count[len];
        memset(count, 0, len*4);

        // whether one item has been processed
        bool processed[len];
        for(int i=0; i<len; i++){
            processed[i] = false;
        }

        // maintain a queue
        int array[len+1];
        array[0] = 0;
        int head = 0, tail = 1;
        while(head < tail){ // to be update
            int start = array[head];
            int step = nums[start];
            for(int i=1; start+i<len && i<=step; i++){
                if (! processed[start+i]){
                    array[tail] = start + i;
                    count[start+i] = count[start] + 1;
                    tail += 1;
                    processed[start + i] = true;
                    if (start + i == len-1){
                        return count[start + i];
                    }
                }
            }
            head += 1;
        }
        return count[len-1];
    }

    int solve_fast(vector<int>& nums){
        int step =0, head=0, tail=0;
        while(tail<nums.size()-1 && head<=tail){
            int tail_new = tail;
            for(int i=head; i<=tail; i++)
                tail_new = max(tail_new, i+nums[i]);
            // Since the solution is guaranted to exist, after for loop ends, 
            // the current head & tail will always be updated, head will move to tail + 1
            head = tail + 1; 
            tail = tail_new;
            step += 1;
        }
        return step;
    }

    int jump(vector<int>& nums){
        return solve_fast(nums);
    }
};

int main(){
    vector<int> nums{2, 3, 1, 1, 4};
    Solution sol;
    int res = sol.jump(nums);
    cout << res << "\n";
}
