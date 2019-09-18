/* 35. Search Insert Position. https://leetcode.com/problems/search-insert-position/
 */
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    int bin_search_left(vector<int> &nums, int target){
        int start=0, end=nums.size();
        while(start < end){
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
public:
    int searchInsert(vector<int>& nums, int target) {
        return bin_search_left(nums, target);
    }
};

int main(){
    vector<int> nums = {1,3,5,6};
    int target = 5;
    Solution solution;
    int res = solution.searchInsert(nums, target);
    cout << res << "\n";
}
