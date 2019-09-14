/* 31. Next Permutation. https://leetcode.com/problems/next-permutation/
 * Solution refer to the official solution
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        bool success=false;
        for(int i=nums.size()-1; i>0; i--){
            if(nums[i] > nums[i-1]){
                for(int j=nums.size()-1; j>=i; j--){
                    if(nums[j] > nums[i-1]){
                        swap(nums[j], nums[i-1]);
                        success = true;
                        break;
                    }
                }
                reverse(nums, i, nums.size()-1);
                break;
            }
        }
        if (! success){
            reverse(nums, 0, nums.size()-1);
        }
    }
    void reverse(vector<int>& nums, int begin, int end){
        int i=begin, j=end;
        while(i<j){
            swap(nums[i], nums[j]);
            i++;
            j--;
        }
    }
};

int main(){
    int array[] = {2,3,4,1};
    //int array[] = {3,2,1};
    auto n = sizeof(array)/sizeof(array[0]);
    vector<int> nums(array, array+n);
    Solution solution;
    solution.nextPermutation(nums);
    //solution.reverse(nums, 0, 0);
    for (int i=0; i<nums.size(); i++){
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}
