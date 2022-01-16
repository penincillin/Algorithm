/*
 * Shuffle an Array, https://leetcode.com/problems/shuffle-an-array/
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;

class Solution {
private:
    vector<int> nums;
public:
    Solution(vector<int>& nums) {
        this->nums = nums;
    }
    
    vector<int> reset() {
        return nums;
    }
    
    vector<int> shuffle() {
        return solve_02();
    }

    vector<int> solve_01(){
        int N = nums.size();
        vector<int> nums_tmp = nums;
        vector<int> res;
        while (N>0){
            int rand_idx = rand() % N;
            res.push_back(nums_tmp[rand_idx]);
            nums_tmp.erase(nums_tmp.begin() + rand_idx);
            N--;
        }
        return res;
    }

    vector<int> solve_02(){
        int N = nums.size();
        vector<int> res;
        for (int i=0; i<N; i++){
            res.push_back(nums[i]);
            int rand_idx = rand()%(i+1);
            swap(res[i], res[rand_idx]);
        }
        return res;
    }
};

void print_vec(vector<int>& nums){
    for (auto it=nums.begin(); it!=nums.end(); it++){
        cout << *it << " ";
    }
    cout << "\n";
}

string vector2str(vector<int> &nums){
    string res = "";
    for (auto it=nums.begin(); it!=nums.end(); it++){
        res += char(*it+'0');
    }
    return res;
}

int main(){
    srand (time(NULL));

    vector<int> nums = {1,2,3};
    Solution solution(nums);
    map<string, int> stat;

    int N = 1000000;
    for (int i=0; i<N; i++){
        vector<int> nums_origin = solution.reset();
        vector<int> nums_shuffle = solution.shuffle();
        // string num_str_origin = vector2str(nums_origin);
        string num_str_shuffle = vector2str(nums_shuffle);
        if (stat.find(num_str_shuffle) != stat.end()){
            stat[num_str_shuffle] += 1;
        }
        else{
            stat[num_str_shuffle] = 1;
        }
    }

    for (auto it=stat.begin(); it!=stat.end(); it++){
        cout << it->first << " " << 1.0*it->second/N << "\n";
    }

    return 0;
}
