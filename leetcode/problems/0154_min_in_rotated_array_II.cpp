/* 153. Find Minimum in Rotated Sorted Array. https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 */

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums){
        return _findMin2(nums);
    }
private:
    int _findMin1(vector<int> nums){
        /* this solution is o(n) complexity, since given the worst case, the complexity is no better than o(n), 
         * The worst case is [1,1,1,1,0,1,1,1,1], since this '0' can appear in any position, 
         * then there is no better solution than o(n) to determine it
         */
        int res = nums[0];
        for (int i=1; i<nums.size(); i++){
            res = min(res, nums[i]);
        }
        return res;
    }

    int _findMin2(vector<int> nums){
        /* this idea is kind of like quick sort, although its worst case is still o(n), it its average complexity is better than o(n)
         * Although the rotated array is more complex than the sorted array, it can be divied into two cases, where the rotate point on the first half and the rotate point on the right half.
        */
        int head=0, tail=nums.size();
        while(head < tail){
            int mid=(head+tail)/2;
            if (nums[mid] > nums[tail]){ // rotate point on the right half
                head = mid+1;
            }
            else if(nums[mid] < nums[tail]){ // rotate point on the left half
                tail = mid;
                
            }
            else{
                tail--;
            }
        }
        return nums[head];
    }
};

int main(){
    vector<int> nums = {4,5,6,7,0,1,2};
    //vector<int> nums = {2,2,2,0,1};
    //vector<int> nums = {10,1,10,10,10};
    //vector<int> nums = {1,1,0,1,1,1,1,1,1,1,1,1};
    Solution solution;
    int res = solution.findMin(nums);
    cout << res << "\n";
    return 0;
}
