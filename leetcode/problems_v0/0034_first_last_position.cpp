/* 34. Find First and Last Position of Element in Sorted Array. https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 * The idea is to use two kinds of binary search method. That returns the leftmost and rightmost index
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    int bin_search_left(vector<int>& nums, int target){
        // return value is i, then a[i:]>=x and a[:i]<x
        int start=0, end=nums.size();
        while (start<end){
            int mid = (start+end)/2;
            if (nums[mid] < target){
                start = mid+1;
            }
            else{
                end = mid;
            }
        }
        return start;
    }

    int bin_search_right(vector<int>& nums, int target){
        // return value is i, then a[:i]<=x and a[i:]>x
        int start=0, end=nums.size();
        while (start<end){
            int mid = (start+end)/2;
            if (target < nums[mid]){
                end = mid;
            }
            else{
                start = mid+1;
            }
        }
        return start;
    }


public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left_idx = bin_search_left(nums, target);
        int right_idx = bin_search_right(nums, target);
        if (right_idx<1 || left_idx>=nums.size()){
            vector<int> res = {-1, -1};
            return res;
        }
        else if (nums[left_idx]!=target || nums[right_idx-1]!=target){
            vector<int> res = {-1, -1};
            return res;
        }
        else{
            vector<int> res = {left_idx, right_idx-1};
            return res;
        }
    }
};

int main(){
    //vector<int> nums = {5,7,7,8,8,10};
    //int target = 8;
    vector<int> nums = {2,2};
    int target = 3;
    Solution solution;
    vector<int> res = solution.searchRange(nums, target);
    cout << res[0] << " " << res[1] << "\n";
}
