#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left=0, right=height.size()-1, max_size=0;
        while(left < right){
            int size = (right-left)*min(height[left],height[right]);
            max_size = max(max_size, size);
            if(height[left] < height[right]) 
                left++;
            else             
                right--;
        }
        return max_size;
    }
};

int main(){
    int A[] = {1,2,1};
    vector<int> height(A, A+3);
    Solution ss;
    cout << ss.maxArea(height) << endl;
    return 0;
}
