#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        return _search(nums, target, 0, nums.size()-1);
    }
private:
    int bin_search(vector<int> nums, int target, int head, int tail){
        while (tail-head>=1){
            int mid = (head+tail)/2;
            if (nums[mid]>=target){
                tail = mid;
            }
            else{
                head = mid+1;
            }
        }
        return head;
    }
    int _search(vector<int> nums, int target, int head, int tail){
        int res = -1;
        if (head > tail){
            return -1;
        }
        if (head == tail){
            if (nums[head] == target){
                return head;
            }
            else{
                return -1;
            }
        }
        int mid = (head+tail)/2;
        if (nums[mid] == target){
            return mid;
        }
        else{
            if (head<=mid-1){ // corner case check
                if (nums[head]<=nums[mid-1]){ // which means the L[head:mid] is well sorted, then we could conduct bin_search on this sub-set
                    int tmp_res = bin_search(nums, target, head, mid-1);
                    if (nums[tmp_res] == target){
                        return tmp_res;
                    }
                    else{
                        return _search(nums, target, mid+1, tail);
                    }
                }
                else{
                    int tmp_res = bin_search(nums, target, mid+1, tail);
                    if (nums[tmp_res] == target){
                        return tmp_res;
                    }
                    else{
                        return _search(nums, target, head, mid-1);
                    }
                }
            }
            else{
                return _search(nums, target, mid+1, tail);
            }
        }
    }
};

int main(){
    vector<int> nums = {4,5,6,7,0,1,2};
    int target = 0;
    Solution solution;
    int res = solution.search(nums, target);
    cout << res << "\n";
    return 0;
}
