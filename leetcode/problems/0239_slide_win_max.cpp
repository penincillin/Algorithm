/* 239. Sliding Window Maximum https://leetcode.com/problems/sliding-window-maximum/
 * The solution use deque, refers to: https://leetcode.com/problems/sliding-window-maximum/discuss/65956/My-C%2B%2B-O(n)-deque-based-solution-with-explanation
 * The solution pass the whole array twice, from left to right and from right to left. Detailed idea could be found https://leetcode.com/problems/sliding-window-maximum/discuss/65881/O(n)-solution-in-Java-with-two-simple-pass-in-the-array
*/

#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        //return solve_deque(nums, k);  
        return solve_two_pass(nums, k);
    }

    vector<int> solve_two_pass(vector<int>& nums, int k){
        vector<int> res;
        int n = nums.size();
        if (n<=0) {
            return res;
        }
        int left_maxium[n];
        int right_maxium[n];
        int left_max, right_max;
        for(int i=0; i<n; i++){
            if (i%k == 0){
                left_max = nums[i];
            }
            else{
                left_max = max(left_max, nums[i]);
            }
            left_maxium[i] = left_max;
            if (i==0 || (n-i)%k==0){
                right_max = nums[n-i-1];
            }
            else{
                right_max = max(nums[n-i-1], right_max);
            }
            right_maxium[n-i-1] = right_max;
        }
        for (int i=0; i<n-k+1; i++){
            res.push_back( max(left_maxium[i+k-1], right_maxium[i]) );
        }
        return res;
    }

    vector<int> solve_deque(vector<int> &nums, int k){
        deque<int> my_deque;
        vector<int> res;
        for(int i=0; i<nums.size(); i++){
            while(! my_deque.empty() && nums[my_deque.back()]<nums[i]){
                my_deque.pop_back();
            }
            my_deque.push_back(i);
            if (i>=my_deque.front()+k){
                my_deque.pop_front();
            }
            if (i>=k-1){
                res.push_back(nums[my_deque.front()]);
            }
        }
        return res;
    }
};

int main(){
    vector<int> nums = {1,3,-1,-3,5,3,6,7}; 
    int k = 3;
    Solution solution;
    vector<int> res = solution.maxSlidingWindow(nums, k);
    for(int i=0; i<res.size(); i++){
        cout << res[i] << " ";
    }
    cout << "\n";
}
