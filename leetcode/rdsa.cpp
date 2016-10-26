/* Too easy to write anything */

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() <=1){
            return nums.size();
        }
        else{
            int non_dupli = 1;
            int prev = nums[0];
            while(non_dupli < nums.size()){
                if(nums[non_dupli] != prev){
                    prev = nums[non_dupli];
                    non_dupli += 1;
                }
                else{
                    nums.erase(nums.begin()+non_dupli);
                }
            }
            return non_dupli;
        }
    }
};
int main(){

}
