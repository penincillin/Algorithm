#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;


struct Node{
    int posi;
    int value;
};

bool cmp(Node n1, Node n2){
    return n1.value < n2.value;
}

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        vector<Node> nodes;

        for (int i=0; i<nums.size(); i++){
            Node tmp_node;
            tmp_node.posi = i;
            tmp_node.value = nums[i];
            nodes.push_back(tmp_node);
        }

        sort(nodes.begin(), nodes.end(), cmp);

        vector<Node>::iterator begin=nodes.begin(), end=nodes.end();
        end--;

        while(begin!=end){
            int left = begin->value, right=end->value;
            int tmpRes = left+right;
            if (tmpRes>target) end--;
            if (tmpRes<target) begin++;
            if (tmpRes==target){
                int first = begin->posi+1, second = end->posi+1;
                if (first>second) swap(first, second);
                result.push_back(first);
                result.push_back(second);
                break;
            }
        }
        return result;
    }
};

int main(){
    int numbers[4] = {0,4,3,0};
    int target = 7;
    vector<int> nums;
    for (int i=0; i<4; i++) nums.push_back(numbers[i]);
    Solution solve;
    vector<int> res = solve.twoSum(nums, target);
    for(int i=0; i<res.size(); i++)
        cout << res[i] << endl;
}
