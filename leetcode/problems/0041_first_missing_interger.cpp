/* 41. First Missing Positive. https://leetcode.com/problems/first-missing-positive/
 * The key idea is to use the index of orginal array to store the result.
 */

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for(int i=0; i<nums.size(); i++){
            /*
            if (i==3){
                cout << "index " << nums[i]-1 << "\n";
                cout << "nums[index] " << nums[nums[i]-1] << "\n";
                cout << "nums[i] " << nums[i] << "\n";
            }
            */
            while (nums[i]>0 && nums[i]-1<nums.size() && nums[nums[i]-1] != nums[i]){
                    swap(nums[nums[i]-1], nums[i]);
            }
            /*
            cout << "=======" << i << "======\n";
            for(int i=0; i<nums.size(); i++){
                cout << nums[i] << " ";
            }
            cout << "\n";
            */
        }
        for(int i=0; i<nums.size(); i++){
            if(nums[i] != i+1){
                return i+1;
            }
        }
        return nums.size()+1;
    }
};

int main(){
    //vector<int> nums = {7,8,9,11,12};
    vector<int> nums = {-1,4,2,1,9,10};
    Solution solution;
    int res = solution.firstMissingPositive(nums);
    cout << res << "\n";
}
